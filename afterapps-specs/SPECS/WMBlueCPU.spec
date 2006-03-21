%define prefix /usr
%define name WMBlueCPU
%define version 0.6
%define release 2

Summary: WMBlueCPU is a cpu monitor.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sheepmakers.ath.cx/utils/wmbluecpu/
Source0: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMBlueCPU is a cpu monitor. It runs either as a dockapp or
in a normal window. It displays the number of the cpu being
monitored in the top left corner, the cpu usage in the top
right corner, and a usage history chart at the bottom.

%prep
%setup -q -n WMBlueCPU

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 wmbluecpu $RPM_BUILD_ROOT%prefix/bin
install -m 644 wmbluecpu.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL README THANKS


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1
- Initial build.



