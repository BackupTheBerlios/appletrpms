%define		name peksystray
%define		version 0.4.0
%define		release 5%{?dist}

Summary:	a dockable systray
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://sourceforge.net/projects/peksystray/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-ldadd.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	glibc
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	glibc-devel

%description
PekSysTray is a system tray "notification area" dockapp similar to the GNOME
notification area applet. But it's designed for any window manager supporting 
docking.

%prep
%setup -q
%patch0

%build

CFLAGS="-lX11" \
./configure --prefix=%{_prefix} --libdir=%{_libdir}

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 src/peksystray $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.4.0-5
- updated sourceforge URLs

* Mon Dec 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.4.0-4
- cleanup of spec file.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.4.0-3
- added patch from Gentoo for build under x86_64.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.0-2
- added distro info to release.

* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.0-1
- New version.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-5
- updated URL and Source info.

* Wed May 25 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-4
- changed to build with FC5 (X11R7).

* Wed Apr  5 2006 Sean Dague <sean@dague.net> - 0.3.0-3
- remove -lX11 which was breaking things

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-2
- changed prefix path to /usr.

* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-1
- New version.

* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-1
- Initial build.
