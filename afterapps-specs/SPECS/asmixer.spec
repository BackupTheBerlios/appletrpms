%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name asmixer
%define version 0.5
%define release 2

Summary: AS Sound Mixer Applet
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program is designed to rain fire and brimstone upon a thousand lands
crushing an infinite number of souls with devestation never before experienced
by man.  Either that, or it might just be a simple
Mixer Utility for Linux systems.  Requires /dev/mixer to work.  The
3 buttons are quite simply Volume, CD, and PCM.

And of course, asmixer looks best under the Afterstep WM!

%prep
%setup -q

%build
./configure --prefix=%{__prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc INSTALL README


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> 0.5-2
- changed prefix path to /usr.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - Aug 30, 2003
- Initial build.


