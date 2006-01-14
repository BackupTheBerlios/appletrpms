%define prefix /usr/X11R6
%define name wmtemp
%define version 0.0.5
%define release 1

Summary: wmtemp displays CPU & SYS temps in "LCD look" via lm_sensors.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://gnodde.org/wmtemp/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: lm_sensors

%description
wmtemp dockapp displays CPU & SYS temps in LCD look via lm_sensors. 

%prep
%setup -q -n %{name}

%build
make DEST=%prefix/bin

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 wmtemp $RPM_BUILD_ROOT%prefix/bin/
install -m 644 wmtemp.1x $RPM_BUILD_ROOT%prefix/man/man1/wmtemp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc COPYING CREDITS ChangeLog README


%changelog
* Sat Jan 14 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.0.5-1
- Initial build.



