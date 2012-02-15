%define		name wmsystray
%define		version 0.1.1
%define		release 6%{?dist}

Summary:	wmsystray is a dockable systray
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://kai.vm.bytemark.co.uk/~arashi/wmsystray/
Source0:	http://kai.vm.bytemark.co.uk/~arashi/wmsystray/release/%{name}-%{version}.tar.bz2
Patch0:		%{name}-fix-warnings.diff
Patch1:		%{name}-optflags.diff
Patch2:		%{name}-%{version}-Makefile.patch
Patch3:		%{name}-%{version}-Rules.make.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXpm-devel

%description
wmsystray is meant to be used as a Window Maker dock applet.
wmsystray provides a notification area, or "system tray", in a
manner compliant with freedesktop.org's System Tray Protocol
Specification[1]. This allows wmsystray to serve as a system
tray area for recent GNOME and KDE applications, and should
work for applications from GNOME 2.x and later or KDE 3.x and
later.

%prep
%setup -q

%patch0
%patch1
%patch2
%patch3

%build
make %{?_smp_mflags} prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

make prefix=%{_prefix} destdir=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS HACKING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-6
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-5
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-4
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-3
- changed prefix path to /usr.

* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-2
- Added .diff patch files (thanks, suse).

* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.1-1
- Initial build.



