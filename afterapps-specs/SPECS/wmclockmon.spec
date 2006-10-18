%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmclockmon
%define version 0.8.1
%define release 3

Summary: digital clock with 7 different styles in either LCD or LED style
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tnemeth.free.fr/projets/dockapps.html
Source0: http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmclockmon is a nice digital clock with 7 different styles in either
LCD or LED style; uses locales to display weekday and month names.
It also features the internet time.
Includes wmclockmon-cal, a calendar display and wmclockmon-config,
a configuration tool for the package.
Sample .wmclockmonrc files are included in with the doc files. 

%prep
%setup -q

%build
./configure --prefix=%{__prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wmclockmon/

rm -rf styles/Makefile*

install -m 644 styles/* $RPM_BUILD_ROOT%{_datadir}/wmclockmon/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}*
%{_mandir}/man1/*
%dir %{_datadir}/wmclockmon
%{_datadir}/wmclockmon/*
%doc doc/sample*.wmclockmonrc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README THANKS TODO

%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-2
- changed prefix path to /usr.

* Sun Apr 10 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-1
- Updated to 0.8.1.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-2
- Changed styles dir to /usr/X11R6/share from /usr/share.

* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-1
- Initial build.

