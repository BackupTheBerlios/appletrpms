%define name	hvclock
%define version	1.0.2
%define release	2%{?dist}

Summary:	a dockapp analog clock and calendar application
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www2.hugovil.com:8080/en/hvclock/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	glibc
Requires:	gtk2
Requires:	libICE
Requires:	libpng
Requires:	libSM
Requires:	libX11
Requires:	pango
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gtk2-devel
BuildRequires:	libICE-devel
BuildRequires:	libpng-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	pango-devel

%description
hvclock is a "DockApp" analog clock and calendar application.
Versions 1.0.0 and later provide anti-aliasing via Cairo.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/hvclock
%{_mandir}/man1/hvclock.*
%doc AUTHORS COPYING ChangeLog NEWS README TODO

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2-2
- updated spec file.

* Wed Mar 23 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.0.2-1
- new version.

* Thu Dec 09 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-1
- new version.

* Thu Jan 07 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.2.0-2
- added distro info to release.

* Sat Sep 09 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.2.0-1
- new version.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-2
- changed prefix path to /usr.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.0-1
- Initial build.



