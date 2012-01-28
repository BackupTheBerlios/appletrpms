%define		name wmab
%define		version 0.3
%define		release 1%{?dist}

Summary:	laptop dockapp to graphically monitor power sources status using ACPI.
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://web.tiscali.it/kalem/dockapps.html
Source0:	http://web.tiscali.it/kalem/wmab/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-libacpi.c.patch
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
WMab is a WindowMaker dockapp that allows ACPI laptop users 
to graphically monitor their power sources status. I.e. whether 
or not AC or batteries are in use as well as how long it will 
take to drain or charge the batteries.

%prep
%setup -q

# /proc/acpi/info was deprecated in kernel 2.6.36, let's try 
# /sys/module/acpi/parameters/acpica_version instead.
%patch0

%build
cd wmab

make INCDIR=' -I%{_includedir}' LIBDIR=' -L%{_libdir}'

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 wmab/wmab $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/wmab
%doc BUGS CHANGES COPYING README TODO

%changelog
* Fri Oct 28 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.3-1
- initial release.
