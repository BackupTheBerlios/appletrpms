%define name wmsm.app
%define version 0.2.1
%define release 5%{?dist}

Summary: WindowMaker System Monitor
Name: %name
Version: %version
Release: %release
License: GPLv2+
Group: AfterStep/Applets
URL: http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html
Source0: http://www.unetz.com/schaepe/DOCKAPPS/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
WindowMaker System Monitor.

Monitors:
    * Processor Load
    * Memory Load
    * Swap Load
    * Disk I/O (Read/Write)
    * Uptime

%prep
%setup -q

%build
cd wmsm
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd wmsm
install -s -m 755 wmsm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING INSTALL
%{_bindir}/wmsm


%changelog
* Sun Apr 04 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-5
- dead link, pointed to ftp.afterstep.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-2
- changed prefix path to /usr.

* Sat Dec 31 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-1
- New version.

* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.2.0-1
- Initial build.
