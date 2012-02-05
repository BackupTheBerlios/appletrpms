%define		name wmlaptop
%define		version 1.4
%define		release 1%{?dist}

Summary:	WindowMaker dockapp that includes all that a linux user with a laptop needs 
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/227
Source0:	http://dockapps.windowmaker.org/download.php/id/509/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.patch
Patch1:		%{name}-%{version}-ACPI-detection.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
wmlaptop is a WindowMaker dockapp that includes all that a linux user with a laptop needs:
* Battery estimated time remaining
* Multi Batteries support
* Battery remaining charge (visual and percent)
* Auto-Frequency Scaling
* Manual Frequency Scaling
* 0-100 Cpu Load indicator
* APM and ACPI support
* sysfs and /proc filesystems support
* Kernel 2.6 series fully compatible

%prep
%setup -q
%patch0
%patch1

%build
make LIBDIR='-L%{_libdir}'

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}

make install INSTALLDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS BUGS CHANGELOG LICENSE README README.IT THANKS

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.4-1
- initial build.
