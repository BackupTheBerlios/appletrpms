%define		name wmtz
%define		version 0.7.1
%define		release 2%{?dist}

Summary:	dockapp displays the local time from different zones
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/24
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
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
wmtz is a Window Maker dock app derived from the WMiNET
dock app. It displays the local time from different time zones
defined in the configuration file. It can also display the
current Julian Day Number as well as Swatch beats and  
sidereal time at Greenwich and local sidereal time and 
local time, date and weekday.

This app can be useful (?) for people who have to communicate 
in realtime with people from different time zones. It allows 
you to avoid making a fool of yourself by calling someone 
when they are asleep...

%prep
%setup -q -n %{name}-0.7

%build
cd wmtz

make LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -s -m 755 wmtz/wmtz $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmtz/wmtz.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 wmtz/wmtzrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/wmtz
%{_mandir}/man1/wmtz.1*
%{_sysconfdir}/wmtzrc
%doc BUGS CHANGES COPYING README wmtz/wmtzrc

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.7.1-2
- shifted URLs to http://dockapps.windowmaker.org.

* Sun Oct 10 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.7.1-1
- new version.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.7-6
- changed URL info to dockapps.org.

* Wed Feb 03 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.7-5
- update source link.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.7-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.7-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.7-2
- changed prefix path to /usr.

* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.7-1
- Initial build.
