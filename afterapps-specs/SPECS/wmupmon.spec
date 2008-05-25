%define name wmupmon
%define version 0.1.3
%define release 5%{?dist}

Summary: DockApp that displays your system uptime in realtime
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
DockApp that displays your system uptime in realtime.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 src/wmupmon $RPM_BUILD_ROOT%{_bindir}/
install -m 644 doc/wmupmon.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS ChangeLog INSTALL THANKS README COPYING


%changelog
* Sat Apr 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-5
- Website is no longer available. Moved links to ftp.afterstep.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-2
- changed prefix path to /usr.

* Wed Mar 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-1
- Initial build.

