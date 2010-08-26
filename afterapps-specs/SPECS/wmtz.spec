%define		name wmtz
%define		version 0.7
%define		release 6%{?dist}

Summary:	wmtz displays the local time from different time zones
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://www.dockapps.org/file.php/id/24
Source0:	http://www.dockapps.org/download.php/id/38/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch
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
%setup -q
%patch0

%build
cd wmtz

make DESTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 wmtz/wmtz $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmtz/wmtz.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc BUGS CHANGES COPYING README wmtz/wmtzrc

%changelog
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
