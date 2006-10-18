%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmupmon
%define version 0.1.3
%define release 3

Summary: DockApp that displays your system uptime in realtime
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://j-z-s.com/projects/index.php?project=wmupmon
Source0: http://j-z-s.com/projects/downloads/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DockApp that displays your system uptime in realtime.

%prep
%setup -q

%build
./configure --prefix=%{__prefix}
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
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-2
- changed prefix path to /usr.

* Wed Mar 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-1
- Initial build.

