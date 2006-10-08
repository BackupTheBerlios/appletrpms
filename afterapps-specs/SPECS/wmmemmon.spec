%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmmemmon
%define version 1.0.2pre2
%define release 5

Summary: WMMemMon - A dockapp to monitor memory/swap usages
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://seiichisato.jp/dockapps/
Source0: http://seiichisato.jp/dockapps/src/%{name}-%{version}.tar.gz
Patch0: wmmemmon-1.0.2-main.c.patch
BuildRoot: %{_tmppath}/%{name}-%{version}pre2-%{release}-buildroot

%description
WMMemMon is a program to monitor memory/swap usages. It is a dockapp that is
supported by X window managers such as Window Maker, AfterStep, BlackBox, and
Enlightenment.
The current memory usage is displaied as the outside pie-slices.  The swap usage
is represented by the inside slices. It has an LCD look-alike user interface.
The back-light may be turned on/off by clicking the mouse button over the
appliacation. If the usage hits a certain threshold, an alarm-mode will alert
you by turning back-light on.

%prep
%setup -q -n %{name}-%{version}
%patch0

%build
./configure --prefix=%{__prefix} --mandir=%{_mandir}
make

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wmmemmon/icons/
install -m 644 icons/* $RPM_BUILD_ROOT%{_datadir}/wmmemmon/icons/

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/wmmemmon/icons
%{_datadir}/wmmemmon/icons/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2pre2-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2pre2-4
- changed prefix path to /usr.

* Sat Mar 11 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2pre2-3
- changed name on RPM to reflect "pre" status.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2pre2-2
- patched main.c paths

* Sat Jun 25 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2pre2-1
- new version

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-1
- Initial build
