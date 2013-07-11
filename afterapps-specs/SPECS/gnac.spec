%define name	gnac
%define version	0.2.4.1
%define release	1%{?dist}

Summary:	GTK2/Gnome audio convertion application
Name:		%name
Version:	%version
Release:	%release
License:	GPLv3+
Group:		Applications/Multimedia
URL:		http://gnac.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	cairo-gobject
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	gstreamer
Requires:	gstreamer-plugins-base
Requires:	gtk3
Requires:	libnotify
Requires:	libxml2
Requires:	pango
Requires:	glib2
Requires:	glibc
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	cairo-gobject-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk3-devel
BuildRequires:	libnotify-devel
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel

%description
Gnac is an easy to use audio conversion program for 
the Gnome desktop. It is designed to be powerful but 
simple! It provides easy audio files conversion between 
all GStreamer supported audio formats.

%prep
%setup -q

%build
./autogen.sh

./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_bindir}/gnac
%{_datadir}/applications/gnac.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnac.gschema.xml
%{_datadir}/gnac/profiles/default/*.xml
%{_datadir}/gnac/profiles/*.xml
%{_datadir}/gnac/*.xml
%{_datadir}/gnome/help/gnac/*/figures/gnac-*.png
%{_datadir}/gnome/help/gnac/*/*.page
%{_datadir}/icons/hicolor/*/apps/gnac.png
%{_datadir}/icons/hicolor/*/apps/gnac.svg
%{_datadir}/locale/*/LC_MESSAGES/gnac.mo
%{_datadir}/pixmaps/gnac.png
%{_mandir}/man1/gnac.*

%changelog
* Sat Mar 23 2013 J. Krebs <rpm_speedy@yahoo.com> - 0.2.4.1-1
- New version.

* Mon Apr 30 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.2.4-1
- Initial build.
