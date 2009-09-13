%define name AlsaMixer.app
%define version 0.1
%define release 1%{?dist}

Summary:	WM applet sound mixer utility for Linux systems with ALSA sound driver
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		AfterStep/Applets
URL:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0:	http://gentoo.mirrors.easynews.com/linux/gentoo/distfiles/%{name}-%{version}.tar.gz
Patch0:		AlsaMixer.app-0.1-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	gcc-c++ alsa-lib-devel
Requires:	alsa-lib

%description
AlsaMixer.app is a mixer utility for Linux systems with ALSA sound driver.
It is designed to be docked in Window Maker (and other wms). This utility has
three volume controllers that can be configured to handle any sound source,
he default sources are 'Master', 'PCM' and 'CD' volume. Sound sources can be
easily muted and there is also wheel mouse support.
The whole GUI and command parsing was taken from Mixer.app (see old doc
for URL's), only connection to ALSA driver was added.

%prep
%setup -q
%patch0

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc INSTALL README COPYING

%changelog
* Tue Aug 18 2009 - 0.1-1
- Initial build.



