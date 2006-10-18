%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define _libdir %{__prefix}/lib

%define name wmradio
%define version 0.9
%define release 3

Summary: wmradio is FM radio card applet for WindowMaker
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://gogo.aquasoft.cz/~cermak/wmradio/
Source0: ftp://ftp.afterstep.org/apps/%{name}/%{name}-%{version}.tgz
Source1: %{name}-rpm-README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmradio is FM radio card applet for WindowMaker 

%prep
%setup -q

%build
cp %{SOURCE1} .
./configure --prefix=%{__prefix} --disable-libxosd --disable-gnome --mandir=%{_mandir}/man1
make

%install
rm -rf $RPM_BUILD_ROOT

make MANDIR=%{_mandir}/man1 install DESTDIR=$RPM_BUILD_ROOT

make install-skins DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/

mv $RPM_BUILD_ROOT/share/* $RPM_BUILD_ROOT%{_datadir}/

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
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Mon May 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.
