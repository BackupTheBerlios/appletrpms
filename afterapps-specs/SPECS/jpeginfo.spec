%define	name 	jpeginfo
%define	version	1.6.1
%define	release	1%{?dist}

Summary:	Utility for optimizing/compressing JPEG files
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://www.kokkonen.net/tjko/projects.html
Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libjpeg
Buildrequires:	glibc-devel
Buildrequires:	libjpeg-devel

%description
Jpeginfo prints information and tests integrity of JPEG/JFIF
files. Program can generate informative listings of jpeg files,
and can also be used to test jpeg files for errors (optionally
broken files can be automatically deleted).

%prep

%setup -q

%build
./configure --prefix=%{_prefix}

make

%install
rm -rf $RPM_BUILD_ROOT

make install bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/jpeginfo
%{_mandir}/man1/*
%doc COPYING COPYRIGHT README


%changelog
* Wed Nov 23 2011 J. Krebs <rpm_speedy@yahoo.com> 1.6.1-1
- initial build.
