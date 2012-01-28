%define		name wmacpiload
%define		version 0.2.0
%define		release 1%{?dist}

Summary:	dockapp that monitors temperature, battery, and AC adapter ACPI status
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://wmacpiload.tuxfamily.org/
Source0:	http://wmacpiload.tuxfamily.org/download/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-lib_acpi.h.patch
Patch1:		%{name}-%{version}-thermal.c.patch
Patch2:		%{name}-%{version}-lib_acpi.c.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
wmacpiload is a dockapp that monitors temperature, battery, 
and AC adapter ACPI status in a nice, graphical display. It 
has an LCD look-alike user interface, and is supported by 
X window managers such as Window Maker, AfterStep, BlackBox, 
and Enlightenment.

%prep
%setup -q

# /proc/acpi/info was deprecated in kernel 2.6.36, let's try 
# /sys/module/acpi/parameters/acpica_version instead.
%patch0

# /proc/acpi/thermal_zone was deprecated in kernel 2.6.36, let's try 
# /sys/class/thermal/ instead.
%patch1
%patch2

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir}

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/wmacpiload
%{_mandir}/man1/wmacpiload.*
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO

%changelog
* Fri Oct 28 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.2.0-1
- initial release.
