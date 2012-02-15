%define		name wmusic
%define		version	 1.5.0
%define		release	 7%{?dist}

Summary:	Windowmaker dockapp that remote controls xmms
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://home.jtan.com/~john/wmusic/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.patch
Requires:	xmms >= 1.0.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glib
Requires:	glibc
Requires:	gtk+
Requires:	libX11
Requires:	libXext
Requires:	libXi
Requires:	libXpm
Requires:	libXxf86dga
Requires:	libXxf86vm
Requires:	xmms
BuildRequires:	glibc-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXxf86dga-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	xmms-devel >= 1.0.0

%description
wmusic is a dockapp that remote-controls xmms. Here is a list
of the features:

- VCR style controls including fast rewind and fast forward
- Time and Playlist position display
- Super stylee rotating arrow
- Hiding of the xmms windows (on startup and through middle-click)

%prep
%setup -q
%patch0

%build
./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/wmusic

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-7
- updated spec file.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-6
- added requires and buildrequires.

* Fri Sep 28 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-5
- homepage has disappeared pointed Source0 to ftp.afterstep.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-1
- Initial build.



