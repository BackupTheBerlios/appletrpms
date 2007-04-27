%define name Temperature.app
%define version 1.4
%define release 8%{?dist}

Summary: WM applet gets temperature every 15 minutes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.fukt.hk-r.se/~per/temperature
Source0: http://www.fukt.bth.se/~per/temperature/%{name}-%{version}.tar.gz
Patch0: Temperature.app-1.4.as.patch
Patch1: Temperature.app-1.4-frog-5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: wget

%description
This WM applet includes two binaries: "Temperature.app" for AfterStep
>= 2.1.0 and WindowMaker (perhaps other window managers too) and
"Temperature.app.as", a version modified to work with AfterStep < 2.1.0..
The AS version has been modified to work under earlier versions of
AfterStep and will not work properly under WindowMaker.

Additionally, the patch from Frog at:

    http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html
    
has been added to allow for pressure, wind, and windchill.

Temperature.app is a Window Maker applet which fetches local
temperature information every 15 minutes from

    http://weather.noaa.gov

and displays it (in Celsius or Fahrenheit).

%prep
%setup -q -n Temperature.app-%{version}

%patch1 -p1 -b .frog
%patch0 -p1 -b .as

%build
make

mv -f Temperature.app Temperature.app.as
cp -f Temperature.cc.as Temperature.cc

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 Temperature.app $RPM_BUILD_ROOT%{_bindir}/Temperature.app
install -s -m 755 Temperature.app.as $RPM_BUILD_ROOT%{_bindir}/Temperature.app.as

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc ChangeLog INSTALL README COPYING


%changelog
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



