%define		name docker
%define		version 1.5
%define		release 5%{?dist}

Summary:	Docking System Tray
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://icculus.org/openbox/2/docker/
Source0:	http://icculus.org/openbox/2/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-manpage.patch
Patch1:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glib2
Requires:	glibc
Requires:	libX11
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel

%description
Docker is a docking application (WindowMaker dock app) which
acts as a system tray for KDE3 and GNOME2. It can be used to
replace the panel in either environment, allowing you to have
a system tray without running the KDE/GNOME panel.

%prep
%setup -q
%patch0
%patch1

%build
make %{?_smp_mflags} \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/docker
%{_mandir}/man1/docker.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.5-5
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.5-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5-2
- changed prefix path to /usr.

* Tue Aug 09 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.5-1
- Initial build.



