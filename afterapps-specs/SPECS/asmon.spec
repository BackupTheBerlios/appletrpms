%define		name asmon
%define		version 0.71
%define		release 2%{?dist}

Summary:	AS system monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.man
Patch0:		%{name}-%{version}-Makefile.patch
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
A system monitor applet for AfterStep.

%prep
%setup -q
%patch0

%build
rm -rf asmon/asmon
rm -rf asmon/*.o
rm -rf wmgeneral/*.o

cd asmon
make  %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

cd asmon
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/asmon.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changelog COPYING
%{_bindir}/asmon
%{_mandir}/man1/asmon.*

%changelog
* Fri Jan 18 2013 J. Krebs <rpm_speedy@yahoo.com> - 0.71-2
- provided new tarball link.

* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.71-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.65-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.65-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.65-2
- changed prefix path to /usr.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - Aug 30, 2003
- Initial build.
