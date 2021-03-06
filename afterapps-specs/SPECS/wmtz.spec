%define		name wmtz
%define		version 0.7.1
%define		release 2%{?dist}

Summary:	dockapp that displays the local time from different zones
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/24
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-version.patch
Patch1:		%{name}-%{version}-Makefile.patch
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
%patch0
%patch1

%build
cd wmtz

make clean

make %{?_smp_mflags} \
	LIBPATH=%{_libdir} \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir} \
	SYSCONFDIR=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT

cd wmtz

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc BUGS CHANGES COPYING README wmtz/wmtzrc
%{_bindir}/wmtz
%{_mandir}/man1/wmtz.1*
%{_sysconfdir}/wmtzrc


%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.7.1-2
- shifted URLs to http://dockapps.windowmaker.org, added version patch.

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
