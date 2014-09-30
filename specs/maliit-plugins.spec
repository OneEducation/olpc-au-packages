Name:          maliit-plugins
Version:       0.94.2
Release:       2%{?dist}.olpcau1
Summary:       Input method plugins

Group:         System Environment/Libraries
License:       BSD
URL:           http://maliit.org/
Source0:       maliit-plugins-0.94.2.tar

#GitUrl: https://github.com/tchx84/plugins.git
#GitBranch: au2a
#GitCommit: 776341fe06a2e56ea04c7edb111dafeec7d732f6

BuildRequires: dbus-devel
BuildRequires: doxygen
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: maliit-framework-devel
BuildRequires: qt-devel

%description
Maliit provides a flexible and cross-platform input method plugins. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%prep
%setup -q

%build
qmake-qt4 -r CONFIG+=notests CONFIG+=disable-nemo-keyboard LIBDIR=%{_libdir} MALIIT_DEFAULT_PROFILE=olpc-xo

make %{?_smp_mflags} V=1

%install
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot}

find %{buildroot} -name '*.moc' -exec rm -rf {} ';'
find %{buildroot} -name '*.gitignore' -exec rm -rf {} ';'
find %{buildroot} -name '*.olpc-layouts' -exec rm -rf {} ';'

chmod 0644 %{buildroot}%{_bindir}/maliit-keyboard*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README VERSION
%{_bindir}/maliit-keyboard*
%{_libdir}/maliit/plugins/libmaliit-keyboard-plugin.so
%{_datadir}/maliit/plugins
%doc %{_datadir}/doc/maliit-plugins/

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.2-1
- New 0.94.2 release

* Sat Feb  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.0-1
- 0.94.0 release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.1-2
- Remove old layout patch backups

* Fri Nov  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.1-1
- 0.93.1 release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-3
- Remove old layout patch backups

* Wed Oct 31 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-2
- update OLPC keyboard layouts patch

* Mon Oct 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-1
- 0.93.0 and update OLPC keyboard layouts patch

* Tue Oct 16 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-3
- Update layout patches

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-2
- Add patch for olpc XO-Touch keyboard layouts

* Thu Sep 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-1
- 0.92.5 and review fixups

* Tue Aug 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.4-1
- Initial packaging
