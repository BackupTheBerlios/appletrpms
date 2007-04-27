%define name hvclock
%define version 0.2.0
%define release 2%{?dist}

Summary: hvclock is a "DockApp" analog clock and calendar application
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www2.hugovil.com:8080/en/hvclock/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
hvclock is a "DockApp" analog clock and calendar application.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO

%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.2.0-2
- added distro info to release.

* Sat Sep 09 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.2.0-1
- new version.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-2
- changed prefix path to /usr.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-1
- Initial build.



