%define prefix /usr/X11R6
%define name WMBlueClock
%define version 0.1
%define release 1

Summary: WMBlueClock is a nice clock app.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sheepmakers.ath.cx/utils/wmblueclock/
Source0: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMBlueClock is a nice clock app. It runs either as a dockapp
or a normal window. It displays hour, minute, second, day of
week, day of month, month, number of month. It can run in 12
and 24 hour mode.

%prep
%setup -q -n WMBlueClock

%build
#./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 wmblueclock $RPM_BUILD_ROOT%prefix/bin
install -m 644 wmblueclock.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS COPYING README THANKS TODO


%changelog
* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1-1
- Initial build.



