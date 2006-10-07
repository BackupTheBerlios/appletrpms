%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name asmount
%define version 1.0.0
%define release 3

Summary: AfterStep mounter
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tigr.net/afterstep/view.php?applet=asmount/data
Source0: http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet used to mount CDs, floppys, and things
like that by pressing a little icon on the Wharf.

%prep
%setup -q

%build
./configure --prefix=%{__prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 asmount $RPM_BUILD_ROOT%{_bindir}
install -m 644 asmount.man $RPM_BUILD_ROOT%{_mandir}/man1/asmount.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc INSTALL README


%changelog
* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-1
- Initial build.
