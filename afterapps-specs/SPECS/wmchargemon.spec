%define prefix	/usr
%define version 0.2
%define release 1
%define name	wmchargemon

Summary:	displays ACPI battery level and power status.
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Amusements/Games
Source0:	http://dockapps.org/download.php/id/694/%{name}-%{version}.tar.gz
URL:		http://dockapps.org/file.php/id/319
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMChargemon is a simple dockapp showing, in a clear way, the
battery level and the power status of your ACPI-driven laptop.
Low and critical battery levels (on which the applet changes
its color) can be set.

%prep
%setup -q

%build

make PREFIX=%{prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin

install -s -m 755 wmchargemon $RPM_BUILD_ROOT%{prefix}/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog INSTALL README
%{prefix}/bin/*

%changelog
* Sat Sep 23 2006 J. Krebs <rpm_speedy@yahoo.com> 0.2-1
- initial build.
