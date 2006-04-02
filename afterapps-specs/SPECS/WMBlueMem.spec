%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name WMBlueMem
%define version 0.9
%define release 2

Summary: WMBlueMem is a memory monitoring program.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sheepmakers.ath.cx/utils/wmbluemem/
Source0: %{name}.tar.gz
Patch0: %{name}.Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMBlueMem is a memory monitoring program. It runs either as a
dockapp or a normal window. On the top the physical memory
usage is displayed and on the bottom the swap space usage is
displayed.

%prep
%setup -q -n WMBlueMem
%patch0

%build
make PREFIX=%{__prefix}

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
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Sat Oct 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.



