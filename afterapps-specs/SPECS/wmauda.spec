%define		name wmauda
%define		version 0.9
%define		release 1%{?dist}

Summary:	dockapp/applet for controlling Audacious music player
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.netswarm.net/
Source0:	http://www.netswarm.net/misc/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	audacious
Requires:	cairo
Requires:	dbus-glib
Requires:	dbus-libs  
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	glibc
Requires:	gtk2
Requires:	libmcs  
Requires:	libmowgli
Requires:	libpng
Requires:	libX11
Requires:	pango
BuildRequires:	atk-devel
BuildRequires:	audacious-devel
BuildRequires:	cairo-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gtk2-devel
BuildRequires:	libmcs-devel
BuildRequires:	libmowgli-devel
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	pango-devel

%description 
A dockapp/applet for controlling the Audacious music player.

%prep
%setup -q
%patch0

%build

make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/wmauda.*

%changelog
* Sat Apr 07 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- initial build, added gentoo patch for -X11 link.
