%define name WMBlueMem
%define version 0.9
%define release 5%{?dist}

Summary: WMBlueMem is a memory monitoring program
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sheepmakers.ath.cx/utils/wmbluemem/
Source0: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}.tar.gz
Patch0: %{name}.Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
WMBlueMem is a memory monitoring program. It runs either as a
dockapp or a normal window. On the top the physical memory
usage is displayed and on the bottom the swap space usage is
displayed.

%prep
%setup -q -n WMBlueMem
%patch0

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 wmbluemem $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmbluemem.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS COPYING INSTALL README THANKS


%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-5
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-4
- Updated Source path. Sheepmakers site is invalid.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Sat Oct 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.



