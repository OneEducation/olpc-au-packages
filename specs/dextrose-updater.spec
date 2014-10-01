Name:    dextrose-updater	
Version: 6
Release: 1
Summary: Yum-based updater for OLPC-AU

Group:   Applications/Updating
License: GPLv3
URL:     https://github.com/OneEducation/dextrose-updater
Source0: dextrose-updater-6.tar

#GitUrl: https://github.com/OneEducation/dextrose-updater.git
#GitBranch: master
#GitCommit: 29c415c3d51cd1bb56a511bb1bceabb68a08a177

BuildArch: noarch
Packager: Martin Abente Lahaye <tch@sugarlabs.org>

%description
Provides a yum-based system packages updater for One Laptop Per Child Australia

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} REPO="au2a-f20-testing" install
chmod 755 %{buildroot}/etc/NetworkManager/dispatcher.d/dextrose-updater-ifup


%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc 

/usr/sbin/dextrose-updater
/etc/sysconfig/dextrose-updater
/etc/NetworkManager/dispatcher.d/dextrose-updater-ifup

%changelog
* Wed Oct 1 2014 Martin Abente Lahaye <tch@sugarlabs.org> 6-1
- initial package

