%define name Temperature.app
%define version 1.4
%define release 10%{?dist}

Summary: WM applet gets temperature every 15 minutes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.fukt.hk-r.se/~per/temperature
Source0: http://www.fukt.bth.se/~per/temperature/%{name}-%{version}.tar.gz
Patch1: Temperature.app-1.4-frog-5.patch
Patch2: Temperature.app-1.4-gcc43.patch
Patch3: Temperature.app-1.4-Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: wget xorg-x11-fonts-ISO8859-1-75dpi xorg-x11-fonts-ISO8859-1-100dpi

%description
Temperature.app is a Window Maker applet which fetches local
temperature information every 15 minutes from

    http://weather.noaa.gov

and displays it (in Celsius or Fahrenheit).

The patch from Frog at:

    http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html

has been added to allow for pressure, wind, and windchill.


%prep
%setup -q

%patch1
%patch2
%patch3

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make install-x11 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc ChangeLog INSTALL README COPYING


%changelog
* Mon Jun 30 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.4-10
- added patch for gcc43.

* Sat Nov 10 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.4-9
- added Require for xorg-x11-fonts-ISO8859-1-75dpi.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.4-8
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as7
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as6
- changed prefix path to /usr.

* Sat Nov 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as5
- Added require for wget.

* Sat Jun 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as4
- Updated description to include news of AS 2.1.0 compatibility.

* Mon Mar 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as3
- Added build for two binaries, one standard and one for
- AfterStep.

* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as2
- Added Frog's patch to include wind, windchill, and pressure.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as1
- Included AfterStep Wharf patch. Probably now broken under WM.

* Thu Feb 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-1
- Initial build.



