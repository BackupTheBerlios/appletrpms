%define prefix /usr
%define name peksystray
%define version 0.3.0
%define release 3

Summary: peksystray is a dockable systray.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.yuv.info/wmnd/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PekSysTray is a system tray "notification area" dockapp similar to the GNOME
notification area applet. But it's designed for any window manager supporting 
docking.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 src/peksystray $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
* Wed Apr  5 2006 Sean Dague <sean@dague.net> - 0.3.0-3
- remove -lX11 which was breaking things

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-2
- changed prefix path to /usr.

* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-1
- New version.

* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-1
- Initial build.
