%define prefix /usr/X11R6
%define name Temperature.app
%define version 1.4
%define release as2

Summary: WM applet gets temperature every 15 minutes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.fukt.hk-r.se/~per/temperature
Source0: %{name}-%{version}.tar.gz
Patch0: Temperature.app-1.4.as.patch
Patch1: Temperature.app-1.4-frog-5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This WM applet has been modified to work under AfterStep.  Some
WM dock information in the source has been elimated; it may not
work properly under WindowMaker.  It works fine in AfterStep :).

Additionally, the patch from Frog at:

    http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html
    
has been added to allow for pressure, wind, and windchill.

Temperature.app is a Window Maker applet which fetches local
temperature information every 15 minutes from

    http://weather.noaa.gov

and displays it (in Celsius or Fahrenheit).

%prep
%setup -q -n Temperature.app-%{version}

%patch0 -p1 -b .as
%patch1 -p1 -b .frog

%build
#./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 Temperature.app $RPM_BUILD_ROOT%prefix/bin/Temperature.app

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc ChangeLog INSTALL README COPYING


%changelog
* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as2
- Added Frog's patch to include wind, windchill, and pressure.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as1
- Included AfterStep Wharf patch. Probably now broken under WM.

* Thu Feb 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-1
- Initial build.



