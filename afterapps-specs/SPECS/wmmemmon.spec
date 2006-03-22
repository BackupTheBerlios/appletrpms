%define prefix /usr
%define name wmmemmon
%define version 1.0.2pre2
%define release 4

Summary: WMMemMon - A dockapp to monitor memory/swap usages
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tnemeth.free.fr/projets/dockapps.html
Source0: %{name}-%{version}.tar.gz
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
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin/
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1/
mkdir -p $RPM_BUILD_ROOT%prefix/share/wmmemmon/icons/

install -s -m 755 src/wmmemmon $RPM_BUILD_ROOT%prefix/bin/
install -m 644 doc/*.1 $RPM_BUILD_ROOT%prefix/man/man1/
install -m 644 icons/* $RPM_BUILD_ROOT%prefix/share/wmmemmon/icons/

%clean
rm -rf $RPM_BUILD_ROOT

%postun
%prefix/share/wmmemmon/icons/*

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%prefix/share/wmmemmon/icons/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
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
