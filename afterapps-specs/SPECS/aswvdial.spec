%define		name aswvdial
%define		version 1.7
%define		release 7%{?dist}

Summary:	ASwvdial is a dock/wharf/slit app for wvdial
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libxml
Requires:	libXpm
Requires:	wvdial
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libxml-devel
BuildRequires:	libXpm-devel

%description
ASwvdial is a dock/wharf/slit app for wvdial.

%prep
%setup -q -n aswvdial
%patch0

%build
cd aswvdial

make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

cd aswvdial

make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README XPM.readme
%{_bindir}/aswvdial
%{_bindir}/netdown
%{_bindir}/netup

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.7-7
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.7-6
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.7-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.7-4
- changed prefix path to /usr.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-3
- Maker script files install better.

* Sun Jun 12 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-2
- Added require for wvdial (duh).

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-1
- Initial build.
