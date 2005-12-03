%define prefix /usr/X11R6
%define name wmtz
%define version 0.7
%define release 1

Summary: wmtz displays the local time from different time zones.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.geocities.com/jl1n/wmtz/wmtz.html
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmtz is a Window Maker dock app derived from the WMiNET
dock app. It displays the local time from different time zones
defined in the configuration file. It can also display the
current Julian Day Number as well as Swatch beats and  
sidereal time at Greenwich and local sidereal time and 
local time, date and weekday.

This app can be useful (?) for people who have to communicate 
in realtime with people from different time zones. It allows 
you to avoid making a fool of yourself by calling someone 
when they are asleep...

%prep
%setup -q
%patch0

%build
cd wmtz

make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
install -s -m 755 wmtz/wmtz $RPM_BUILD_ROOT%prefix/bin/
install -m 644 wmtz/wmtz.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc BUGS CHANGES COPYING INSTALL README wmtz/wmtzrc

%changelog
* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.7-1
- Initial build.



