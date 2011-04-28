%define name trayer
%define version 1.1
%define release 1%{?dist}

Summary:	A lightweight GTK2-based systray for UNIX desktop
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		User Interface/Desktops
URL:		http://hg.debian.org/hg/collab-maint/trayer
Source0:	http://ftp.de.debian.org/debian/pool/main/t/%{name}/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	glibc
Requires:	glibc
Requires:	gtk2
Requires:	libpng
Requires:	libX11
Requires:	libXmu
Requires:	pango
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	glibc-devel
BuildRequires:	gtk2-devel
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXmu-devel
BuildRequires:	pango-devel

%description
A lightweight GTK2-based systray for UNIX desktop.

%prep
%setup -q -n sargon-trayer-srg-75f4d7e

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 trayer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/trayer
%doc CREDITS COPYING CHANGELOG README TODO

%changelog
* Thu Apr 28 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.1-1
- new version (thanks Team Debian).

* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.0-5
- improved links in Makefile.common patch file.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.0-4
- added build requirement for libXmu-devel.

* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.0-3
- added patch for gtk issues (thanks Team Debian).

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.0-2
- added distro info to release.

* Mon Jun 26 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build.
