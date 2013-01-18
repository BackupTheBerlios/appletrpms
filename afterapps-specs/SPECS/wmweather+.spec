%define		name wmweather+
%define		version 2.13
%define		release 3%{?dist}

Summary:	A dock app for displaying weather information
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://sourceforge.net/projects/wmweatherplus/
Source0:	http://prdownloads.sourceforge.net/wmweatherplus/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libcurl
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	pcre
Requires:	w3c-libwww
Requires:	WINGs-libs >= 0.95.0
BuildRequires:	glibc-devel
BuildRequires:	libcurl-devel
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	pcre-devel
BuildRequires:	w3c-libwww-devel
BuildRequires:	WINGs-devel >= 0.95.0

%description
wmweather+ downloads current conditions, forecast data, and optionally a
radar image. It will also watch for various warnings and display them using an
external command.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--with-libwraster=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README HINTS example.conf
%{_bindir}/wmweather+
%{_mandir}/man1/wmweather+.*

%changelog
* Sat Feb 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.13-3
- added buildrequires and requires for WINGs.

* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.13-2
- updated sourceforge URLs.

* Sat Dec 11 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.13-1
- new version.

* Wed Aug 25 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.12-1
- new version.

* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.11-2
- added compiler link to make for libm.

* Fri Apr 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 2.11-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.9-7
- added distro info to release.

* Wed Oct 25 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-6
- added build require for libwraster.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-4
- changed prefix path to /usr.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.9-3
- Added if requires for pcre.

* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.9-2
- Added require for w3c-libwww.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 2.9-1
- Initial build.


