%define prefix /usr
%define name wmifinfo
%define version 0.09
%define release 3

Summary: wmifinfo shows basic network info for all available interfaces
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.zevv.nl/wmifinfo/
Source0: http://www.zevv.nl/wmifinfo/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmifinfo is a simple applet showing basic network info for
all available interfaces. It shows IP address, netmask,
gateway and MAC address.

Left-button click moves to the next interface, right-button
click calls ifup/ifdown scripts. 

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 wmifinfo $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc README


%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.09-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.09-2
- changed prefix path to /usr.

* Mon Mar 28 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.09-1
- Initial build.
