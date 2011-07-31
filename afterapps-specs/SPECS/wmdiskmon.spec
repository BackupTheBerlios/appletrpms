%define name	wmdiskmon
%define version	0.0.2
%define release	1%{?dist}

Summary:	A dockapp that monitors your disks usage in a portable way
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.dockapps.org/file.php/id/236
Source0:	http://www.dockapps.org/download.php/id/584/%{name}-%{version}.tar.gz
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
wmdiskmon is a dockapp that monitors your disks usage in a portable way, 
using the POSIX command df -P.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

make mandir=%{_mandir} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/wmdiskmon
%{_mandir}/man1/wmdiskmon.*
%doc AUTHORS COPYING ChangeLog README THANKS TODO


%changelog
* Fri Jul 15 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.0.2-1
- Initial build.
