%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmsensormon
%define version 1.2.1
%define release 3

Summary: uses lm_sensors to monitor CPU & sys temps, fan speed, and CPU voltage.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmsensormon.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: lm_sensors-devel >= 2.0
Requires: lm_sensors >= 2.0

%description
Wmsensormon is a doc app for WindowMaker that utilizes lm_sensors to
monitor CPU temp, sys temp, fan speeds, and CPU voltage. It offers
configurable warnings for overheating, and the sensors displayed are
adjustable by the user with command line parameters.

%prep
%setup -q

%build
cd wmsensormon
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 wmsensormon/wmsensormon $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 wmsensormon/wmsensormon.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc CHANGELOG COPYING INSTALL README TODO

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-3
- changed prefix path to /usr.

* Tue Jan 03 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-2
- Fixed summary statement.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-1
- Initial build.
