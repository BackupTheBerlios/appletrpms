%define prefix /usr/X11R6
%define name wmcpum.app
%define version 0.1.0
%define release 1

Summary: WindowMaker CPU Monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WindowMaker CPU Monitor. Requires lm_sensors package.

Monitors:
    * Processor Temperature
    * System Temperature
    * Processor Frequency
    * Processor Fan RPM
    * Processor Voltage

%prep
%setup -q

%build
cd wmcpum
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
cd wmcpum
install -s -m 755 wmcpum $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING INSTALL

%prefix/bin/wmcpum


%changelog
* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-1
- Initial build.


