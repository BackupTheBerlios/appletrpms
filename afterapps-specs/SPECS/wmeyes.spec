%define name wmeyes
%define version 1.2
%define release 5%{?dist}

Summary: wmeyes is a dockapp with moving eyes that follow mouse movement
Name: %name
Version: %version
Release: %release
License: MIT
Group: AfterStep/Applets
URL: http://www.bstern.org/wmeyes/
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.man
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libXmu
Buildrequires: libXmu-devel

%description
wmeyes is a dockapp with moving eyes that follow mouse movement.
This version also allows execition of a command by clicking the icon.

%prep
%setup -q

%build
cp %{SOURCE1} .
xmkmf
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 wmeyes $RPM_BUILD_ROOT%{_bindir}/
install -m 644 wmeyes.man $RPM_BUILD_ROOT%{_mandir}/man1/wmeyes.1
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc ChangeLog README LICENSE


%changelog
* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2-5
- added requires for libXmu and libXmu-devel.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2-4
- added distro info to release.

* Sun Sep 08 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2-3
- changed License line to reflect MIT.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2-2
- changed prefix path to /usr.

* Thu Mar 24 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2-1
- Initial build.
