%define name wmsensormon
%define version 1.2.1
%define release 7%{?dist}

Summary: uses lm_sensors to monitor CPU & sys temps, fan speed, and CPU voltage
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmsensormon.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: lm_sensors-devel >= 2.0, lm_sensors-devel < 3.0
Requires: lm_sensors >= 2.0, lm_sensors < 3.0

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
* Thu Aug 06 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-7
- updated URL info.

* Mon Jun 30 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-6
- updated requires for lm_sensors < 3.0.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-5
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-4
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-3
- changed prefix path to /usr.

* Tue Jan 03 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-2
- Fixed summary statement.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.1-1
- Initial build.
