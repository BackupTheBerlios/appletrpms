%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name asclock
%define version 2.0.12
%define release 4

Summary: Clock Applet
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-%{version}.config
Patch0: %{name}-%{version}.xpm.path.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AfterStep clock applet

%prep
%setup -q
%patch0 -b .old

%build
mv configure configure.old
cp %{SOURCE1} configure
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%name/doc
make BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    DOCDIR=$RPM_BUILD_ROOT%{_datadir}/%name/doc \
    install install.man
install -d $RPM_BUILD_ROOT%{_datadir}/%name
cp -a themes/* $RPM_BUILD_ROOT%{_datadir}/%name


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%name
%{_datadir}/%name
%doc COPYING INSTALL README README.THEMES TODO


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-4
- changed prefix path to /usr.

* Tue Jul 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-3
- Added patches for gcc-4.0 and theme path.

* Sat Aug 30 2003 Sean Dague <sean@dague.net> - 2.0.12-2
- Add in theme support

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 
- Initial build.


