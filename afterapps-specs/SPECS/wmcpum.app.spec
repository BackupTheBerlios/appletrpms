%define name wmcpum.app
%define version 0.1.0
%define release 5%{?dist}

Summary: WindowMaker CPU Monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html
Source0: http://www.unetz.com/schaepe/DOCKAPPS/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: lm_sensors

%description
WindowMaker CPU Monitor. Requires lm_sensors package.

Monitors:
    * Processor Temperature
    * System Temperature
    * Processor Frequency
    * Processor Fan RPM
    * Processor Voltage

%prep
%setup -q

%build
cd wmcpum
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd wmcpum
install -s -m 755 wmcpum $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING INSTALL
%{_bindir}/wmcpum


%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-5
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-4
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-3
- changed prefix path to /usr.

* Wed May 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-2
- Added require for lm_sensors.

* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-1
- Initial build.
