%define prefix /usr
%define name wmalms
%define version 1.1.1
%define release 3

Summary: Applet to manage sensor data: temperature, fan speed, voltage.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.geocities.com/wmalms/
Source0: http://www.geocities.com/%{name}/%{name}-%{version}.tar.gz
Patch0: wmalms-1.1.1-prompt-bypass.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: lm_sensors-devel >= 2.0
Requires: lm_sensors >= 2.0

%description
wmalms monitors data obtained from a sensor chip: temperature, fan speed,
voltage. It can be used as a dockable/swallowed applet with Window Maker
or any window manager that supports swallowing, including gnome, kwm (kde),
fvwm and its clones. Alternatively, you can run wmalms as a normal window
with any window manager. wmalms is designed to suit any hardware supported
by lm_sensors.

%prep
%setup -q
%patch0

%build
./configure --prefix=%prefix --with-rpm
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 wmalms $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc COPYING README manual.html

%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.1.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.1.1-2
- changed prefix path to /usr.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.1.1-1
- Initial build.
