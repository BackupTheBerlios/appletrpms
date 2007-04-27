%define name wmsystray
%define version 0.1.1
%define release 5%{?dist}

Summary: wmsystray is a dockable systray
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://kai.vm.bytemark.co.uk/~arashi/wmsystray/
Source0: http://kai.vm.bytemark.co.uk/~arashi/wmsystray/release/%{name}-%{version}.tar.bz2
Patch1: %{name}-fix-warnings.diff
Patch2: %{name}-optflags.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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

%patch1 -p0 -b .orig
%patch2 -p0 -b .orig

%build
make prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} INSTALL=%{_bindir}/install install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS HACKING README


%changelog
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



