%define name wmradio
%define version 0.9
%define release 7%{?dist}

Summary: wmradio is FM radio card applet for WindowMaker
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://gogo.aquasoft.cz/~cermak/wmradio/
Source0: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tgz
Source1: %{name}-rpm-README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
wmradio is FM radio card applet for WindowMaker 

%prep
%setup -q

%build
cp %{SOURCE1} .
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-libxosd --disable-gnome --mandir=%{_mandir}/man1
make

%install
rm -rf $RPM_BUILD_ROOT

make MANDIR=%{_mandir}/man1 install DESTDIR=$RPM_BUILD_ROOT

make install-skins LIBDIR=%{_libdir}/wmradio/ DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_libdir}/wmradio
%{_libdir}/wmradio/*
%doc README wmradio-rpm-README
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.9-7
- code cleanup.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9-6
- added libdir to configure for build under x86_64.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-5
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-4
- Updated Source path.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Mon May 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.
