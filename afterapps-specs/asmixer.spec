%define prefix /usr/X11R6
%define name asmixer
%define version 0.5
%define release 1

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
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%prefix/bin \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%prefix/man/man1 \
    install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc INSTALL README


%changelog
* Fri Aug 22 2003 Sean Dague <sean@dague.net> - Aug 30, 2003
- Initial build.


