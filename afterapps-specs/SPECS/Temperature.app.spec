%define		name Temperature.app
%define		version 1.5
%define		release 1%{?dist}

Summary:	WM applet gets temperature every 15 minutes
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
# The original homepage and download URLs are active, but dated.
#URL:		http://www.fukt.bsnet.se/~per/temperature/
#Source0:	http://www.fukt.bsnet.se/~per/temperature/%{name}-%{version}.tar.gz
# Get newer version (with Frog's patch) from dockapps.windowmaker.org.
URL:		http://dockapps.windowmaker.org/file.php/id/86
Source0:	http://dockapps.windowmaker.org/download.php/id/816/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.patch
Patch1:		%{name}-%{version}-xpm.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	freetype
Requires:	glibc
Requires:	libgcc
Requires:	libstdc++
Requires:	libX11
Requires:	libXext
Requires:	libXft
Requires:	libXpm
Requires:	wget   
Requires:	xorg-x11-fonts-ISO8859-1-100dpi
Requires:	xorg-x11-fonts-ISO8859-1-75dpi
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXft-devel
BuildRequires:	libXpm-devel

%description
Temperature.app is a Window Maker applet which fetches local
temperature information from http://weather.noaa.gov every 15 
minutes and displays it (in Celsius or Fahrenheit).

%prep
%setup -q
%patch0
%patch1

%build
make %{?_smp_mflags} X11_BINDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

make install-x11 X11_BINDIR=%{_bindir} DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README COPYING
%{_bindir}/Temperature.app

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.5-1
- new version.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.4-12
- updated URLs.

* Sat Aug 09 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.4-11
- updated to Frog Patch v6.

* Mon Jun 30 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.4-10
- added patch for gcc43.

* Sat Nov 10 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.4-9
- added Require for xorg-x11-fonts-ISO8859-1-75dpi.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.4-8
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as7
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as6
- changed prefix path to /usr.

* Sat Nov 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as5
- Added require for wget.

* Sat Jun 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as4
- Updated description to include news of AS 2.1.0 compatibility.

* Mon Mar 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as3
- Added build for two binaries, one standard and one for
- AfterStep.

* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as2
- Added Frog's patch to include wind, windchill, and pressure.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-as1
- Included AfterStep Wharf patch. Probably now broken under WM.

* Thu Feb 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.4-1
- Initial build.



