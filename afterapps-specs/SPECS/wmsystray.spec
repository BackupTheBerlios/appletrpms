%define prefix /usr/X11R6
%define name wmsystray
%define version 0.1.1
%define release 2

Summary: wmsystray is a dockable systray.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://kai.vm.bytemark.co.uk/~arashi/wmsystray/
Source0: %{name}-%{version}.tar.bz2
Patch1: %{name}-fix-warnings.diff
Patch2: %{name}-optflags.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmsystray is meant to be used as a Window Maker dock applet.
wmsystray provides a notification area, or "system tray", in a
manner compliant with freedesktop.org's System Tray Protocol
Specification[1]. This allows wmsystray to serve as a system
tray area for recent GNOME and KDE applications, and should
work for applications from GNOME 2.x and later or KDE 3.x and
later.

%prep
%setup -q

%patch1 -p0 -b .orig
%patch2 -p0 -b .orig

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
install -s -m 755 wmsystray/wmsystray $RPM_BUILD_ROOT%prefix/bin/
install -m 644 doc/wmsystray.1 $RPM_BUILD_ROOT%prefix/man/man1/
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS HACKING README


%changelog
* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-2
- Added .diff patch files (thanks, suse).

* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-1
- Initial build.



