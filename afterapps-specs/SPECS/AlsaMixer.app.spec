%define name AlsaMixer.app
%define version 0.1
%define release 2%{?dist}

Summary:	WM applet sound mixer utility for Linux systems with ALSA sound driver
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/253
Source0:	http://dockapps.windowmaker.org/download.php/id/517/%{name}-%{version}.tar.gz
Patch0:		AlsaMixer.app-0.1-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	alsa-lib
Requires:	glibc
Requires:	libgcc
Requires:	libstdc++
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	alsa-lib-devel
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

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
make %{?_smp_mflags}

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
* Sat Dec 10 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.1-2
- Added requires and buildrequires.

* Tue Aug 18 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.1-1
- Initial build.



