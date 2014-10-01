Summary: Custom bits for OLPC AU
Name:    olpc-au-configs
Version: 0.2
Release: 1
URL:     https://www.laptop.org.au/
License: LGPL
Group:   User Interface/Desktops
Source0: olpc-au-configs-0.2.tar

#GitUrl: https://github.com/OneEducation/olpc-au-configs.git
#GitBranch: master
#GitCommit: 8c0d4872f31394cde7073b5b32f654f8b61e5ce6

Requires: sugar >= 0.101
Requires: olpc-powerd

Requires: gstreamer-plugins-vmetaxv, gstreamer-plugins-marvell-mmp3, libvmeta, libphycontmem
Requires: tuxmath, tuxpaint, tuxpaint-stamps
Requires: art4apps, art4apps-images, art4apps-audio-en
Requires: cntlm
Requires: sugar-services
Requires: harvest-client, harvest-tracker, harvest-monitor
Requires: abc123

BuildArch: noarch

%description
Provide configurations and custom files requied by the OLPC AU deployment

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}

%files
%{_sysconfdir}/*
%{_datadir}/*

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`

# harvest service configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_api_key REPLACE_HARVEST_KEY
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_hostname https://harvest.one-education.org
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type boolean -s /desktop/sugar/collaboration/harvest_editable false
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/collaboration/harvest_reponame au2a-f20-testing

# training server configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/services/training/url https://training.one-education.org/training/report
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type string -s /desktop/sugar/services/training/api_key REPLACE_TRAINING_KEY

# support server configuration
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string -s /desktop/sugar/services/zendesk/url https://oneedu.zendesk.com
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type=string -s /desktop/sugar/services/zendesk/token REPLACE_SUPPORT_KEY
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    --type list --list-type string -s /desktop/sugar/services/zendesk/fields '[21891880,21729904,21729914,21808844]'

# Browse home page
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s -t string /desktop/sugar/browser/home_page "file:///usr/share/sugar/data/browse/index.html"

# enable control panel network hidden network section
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults \
    -s --type boolean /desktop/sugar/extensions/network/conf_hidden_ssid true

#enable harvest-monitor
/bin/systemctl enable harvest-monitor

# enable cntlm
/bin/systemctl enable cntlm

# re-write powerd.conf file with olpcau tweaked version
cp /etc/powerd/powerd.conf.olpcau /etc/powerd/powerd.conf

# re-compile dconf schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas

%changelog
* Fri Sep 26 2014 Martin Abente Lahaye <tch@sugarlabs.org> 0.2.1
- Initial files
