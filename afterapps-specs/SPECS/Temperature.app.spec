%define name Temperature.app
%define version 1.4
%define release 12%{?dist}

Summary: WM applet gets temperature every 15 minutes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.fukt.bsnet.se/~per/temperature/
Source0: http://www.fukt.bsnet.se/~per/temperature/%{name}-%{version}.tar.gz
Patch0: Temperature.app-1.4-frog-6.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: wget xorg-x11-fonts-ISO8859-1-75dpi xorg-x11-fonts-ISO8859-1-100dpi freetype
BuildRequires: gcc-c++

%description
Temperature.app is a Window Maker applet which fetches local
temperature information every 15 minutes from

    http://weather.noaa.gov

and displays it (in Celsius or Fahrenheit).

The v6 patch from Frog at:

    http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html

has been added to allow for pressure, wind, and windchill.


%prep
%setup -q

%patch0

%build
make X11_BINDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc ChangeLog INSTALL README COPYING

%changelog
* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.4-12
- updated URLs.

* Sat Aug 09 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.4-11
- updated to Frog Patch v6.

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



