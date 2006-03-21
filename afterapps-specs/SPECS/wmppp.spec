%define prefix /usr
%define name wmppp
%define version 1.3.0
%define release 2

Summary: wmppp provides a PPP activator and network load monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/net.html
Source0: %{name}-%{version}.tar.gz
Patch0: wmppp-1.3.0-hispeed.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: ppp

%description
SYSADMIN! This will allow users direct access to pppd!

WMPPP features all things the standard pppd offers and gives
you some nice additional features too...

        * Integrated online timer;
        * Integrated modem RX/TX LED's;
		* Integrated WMPPP status LED; 
        * Integrated autoscaling PPP transfer statistics;
		* Integrated CARRIER/CONNECT display;
		* Integrated bytes/second Speed-O-Meter;
		* Automatic detection of active ppp interfaces;
		* User definable scripts for the V and X buttons and
  		  also for 'ifdown' which are read from ~/.wmppprc;
		* 'force' option in /etc/ppp/.wmppprc for sites
  		  where users are not allowed to mess with pppd;
		* Several commandline options (try '-h' for help);

WMPPP is being developped on DEC Alpha machines running Linux
(RedHat-5.0 and RedHat-5.1), but WMPPP is also intensively 
tested on x86 and m68k Linux machines...

%prep
%setup -q -n wmppp.app
%patch0

%build
cd wmppp

make all

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT/etc/ppp
install -s -m 755 wmppp/wmppp $RPM_BUILD_ROOT%prefix/bin/
install -s -m 755 wmppp/getmodemspeed $RPM_BUILD_ROOT/etc/ppp
install -m 644 wmppp/user.wmppprc $RPM_BUILD_ROOT/etc/ppp/wmppprc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
/etc/ppp/*
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO
%doc wmppp/*.wmppprc wmppp/example-scripts/

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-2
- changed prefix path to /usr.

* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-1
- Initial build.



