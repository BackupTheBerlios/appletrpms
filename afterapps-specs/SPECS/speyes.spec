%define name speyes
%define version 1.2.0
%define release 6%{?dist}

Summary: South Park-themed wmeyes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://okb-1.org/speyes/speyes.html
Source0: http://okb-1.org/speyes/%{name}-%{version}.tar.gz
Source1: %{name}.man
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libXmu
Buildrequires: libXmu-devel imake

%description
South Park-themed wmeyes.

%prep
%setup -q

%build
cp %{SOURCE1} .
xmkmf
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 speyes $RPM_BUILD_ROOT%{_bindir}/
install -m 644 speyes.man $RPM_BUILD_ROOT%{_mandir}/man1/speyes.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc CHANGES README COPYING


%changelog
* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-6
- added build require for imake.

* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-5
- added requires for libXmu and libXmu-devel.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-2
- changed prefix path to /usr.

* Wed Mar 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-1
- Initial build.



