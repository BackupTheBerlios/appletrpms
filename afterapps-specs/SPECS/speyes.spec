%define		name speyes
%define		version 1.2.0
%define		release 7%{?dist}

Summary:	South Park-themed xeyes dockapp
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://okb-1.org/speyes/speyes.html
Source0:	http://okb-1.org/speyes/%{name}-%{version}.tar.gz
Source1:	%{name}.man
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXmu
Requires:	libXpm
Requires:	libXt
BuildRequires:	glibc-devel
BuildRequires:	imake
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXmu-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXt-devel

%description
South Park-themed xeyes dockapp.

%prep
%setup -q

%build
cp %{SOURCE1} .

xmkmf

make %{?_smp_mflags} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

%install
rm -rf $RPM_BUILD_ROOT

make BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES README COPYING
%{_bindir}/speyes
%{_mandir}/man1/speyes.*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-7
- updated spec file.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-6
- added build require for imake.

* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-5
- added requires for libXmu and libXmu-devel.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-2
- changed prefix path to /usr.

* Wed Mar 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-1
- Initial build.



