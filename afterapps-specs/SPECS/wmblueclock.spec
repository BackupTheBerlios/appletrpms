%define		name wmblueclock
%define		version 0.4
%define		release 1%{?dist}

Summary:	WMBlueClock is a nice clock app
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.dockapps.org/file.php/id/344
Source0:	http://www.dockapps.org/download.php/id/772/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXft
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
Requires:	libXft-devel
BuildRequires:	libXpm-devel
Obsoletes:	WMBlueClock

%description
WMBlueClock is a nice clock app. It runs either as a dockapp
or a normal window. It displays hour, minute, second, day of
week, day of month, month, number of month. It can run in 12
and 24 hour mode.

%prep
%setup -q -n wmblueclock
%patch0

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 wmblueclock $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmblueclock.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS COPYING README THANKS TODO


%changelog
* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.4-1
- new version. changed URL info to dockapps.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1-5
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1-4
- Updated Source path. Sheepmakers site is invalid.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1-1
- Initial build.


