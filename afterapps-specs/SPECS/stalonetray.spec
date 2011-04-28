%define name	stalonetray
%define version	0.8.1
%define release	1%{?dist}

Summary:	STand Alone TRAY (notification area) implementation
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		User Interface/Desktops
URL:		http://sourceforge.net/projects/stalonetray
Source0:	http://easynews.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libICE
Requires:	libSM
Requires:	libXpm
Requires:	libX11
Requires:	glibc
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libXpm-devel
BuildRequires:	libX11-devel
BuildRequires:	glibc-devel

%description
Stalonetray is a stand-alone freedesktop.org and KDE system tray
(notification area) for X Window System/X11 (e.g. X.Org or XFree86).
It has full XEMBED support and minimal dependencies: an X11 lib only.
Stalonetray works with virtually any EWMH-compliant window manager.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}

make

make check

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README NEWS COPYING AUTHORS ChangeLog stalonetrayrc.sample stalonetray.html stalonetray.xml
%{_bindir}/*
%{_mandir}/man*/*

%changelog
* Sat Dec 11 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-1
- new version.

* Thu Jan 07 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-1
- new version.

* Wed Jan 09 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.7.6-1
- Initial build.
