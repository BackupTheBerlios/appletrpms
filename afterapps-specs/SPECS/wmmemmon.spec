%define prefix /usr/X11R6
%define name wmmemmon
%define version 1.0.1
%define release 1

Summary: WMMemMon - A dockapp to monitor memory/swap usages
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tnemeth.free.fr/projets/dockapps.html
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q

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

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%prefix/share/wmmemmon/icons/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-1
- Initial build

