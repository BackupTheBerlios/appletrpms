%define name docker
%define version 1.5
%define release 4%{?dist}

Summary: Docking System Tray
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://icculus.org/openbox/2/docker/
Source0: http://icculus.org/openbox/2/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Docker is a docking application (WindowMaker dock app) which
acts as a system tray for KDE3 and GNOME2. It can be used to
replace the panel in either environment, allowing you to have
a system tray without running the KDE/GNOME panel.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 docker $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc COPYING README

%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.5-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5-2
- changed prefix path to /usr.

* Tue Aug 09 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.5-1
- Initial build.



