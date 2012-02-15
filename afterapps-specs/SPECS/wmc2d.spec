%define		name wmc2d
%define		version 2.05
%define		release 1%{?dist}

Summary:	dockapp to monitor the coretemp, temperature and cpu frequency
Name:		%name
Version:	%version
Release:	%release
License:	AGPLv3
Group:		AfterStep/Applets
URL:		http://wmc2d.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/Source/%{name}-2011-04-29-17.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libxcb >= 1.7
Requires:	xcb-util >= 0.3.8
BuildRequires:	glibc-devel
BuildRequires:	libxcb-devel >= 1.7
BuildRequires:	xcb-util-devel >= 0.3.8

%description
This is a small dockapp, which shows the core temperature and cpu frequency
from 2 upto 4 cores/cpus and the temperature of upto two ACPI thermal zones,
which are normaly the motherboard temperature.

The name comes from the "core 2 duo", but now more cpu types are supported.

All cpus, which are supported by the linux kernel "coretemp" and "cpufreq"
modules, could be monitored. f.e. core 2, core i.

Only libxcb (X C-language Bindings library) and the standard C library are as
external libraries required.

%prep

%setup -q -n %{name}

%build

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 wmc2d $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README AGPL-3.0.txt
%{_bindir}/%{name}

%changelog
* Sun Oct 09 2011 J. Krebs <rpm_speedy@yahoo.com> - 2.05-1
- new version.

* Sun Aug 29 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.04-1
- initial build.
