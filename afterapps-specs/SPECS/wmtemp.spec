%define name wmtemp
%define version 0.0.6
%define release 2%{?dist}

Summary: wmtemp displays CPU & SYS temps in "LCD look" via lm_sensors
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://gnodde.org/wmtemp/
Source0: http://open-systems.ufl.edu/mirrors/gentoo/distfiles/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: lm_sensors-devel >= 2.0, lm_sensors-devel < 3.0
Requires: lm_sensors >= 2.0, lm_sensors < 3.0

%description
wmtemp dockapp displays CPU & SYS temps in LCD look via lm_sensors. 

%prep
%setup -q -n %{name}

%build
make DEST=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 wmtemp $RPM_BUILD_ROOT%{_bindir}/
install -m 644 wmtemp.1x $RPM_BUILD_ROOT%{_mandir}/man1/wmtemp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc COPYING CREDITS ChangeLog README


%changelog
* Mon Jun 30 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.0.6-2
- updated requires for lm_sensors < 3.0.

* Mon May 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.0.6-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.0.5-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.0.5-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.0.5-2
- changed prefix path to /usr.

* Sat Jan 14 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.0.5-1
- Initial build.
