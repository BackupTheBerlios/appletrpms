%define		name wmcalc
%define		version 0.4
%define		release 7%{?dist}

Summary:	a dockapp calculator
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/130
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-manpage.patch
Patch1:		%{name}-%{version}.Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	glibc
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	glibc-devel

%description
Wmcalc is a 64x64 pixel application that performs all the
functions (and eventually more) of a simple four function
calculator. It includes a 10 digit alpha-numeric display,
and twenty buttons for user input. Clicking on the display
will clear the calculator.

%prep
%setup -q -n wmcalc-%{version}
%patch0
%patch1

%build
make %{?_smp_mflags} \
	PREFIX=%{_prefix} \
	CONF=%{_sysconfdir} \
	MANDIR=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	CONF=%{_sysconfdir} \
	MANDIR=%{_mandir}  install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README wmcalc.conf .wmcalc
%{_bindir}/wmcalc
%{_mandir}/man1/wmcalc.*
%{_sysconfdir}/wmcalc.conf

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.4-7
- shifted URL link to http://dockapps.windowmaker.org.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.4-6
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4-5
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4-4
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4-3
- changed prefix path to /usr.

* Wed Jan 04 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4-2
- Included additional tarball config file.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4-1
- Initial build.
