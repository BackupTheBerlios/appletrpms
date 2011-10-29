### BEGIN Distro Defines
%define mdk  %(if [ -e /etc/mandrake-release ]; then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1

%if %{mdk}
  %define generic 0
%endif

%if %{fedora}
  %define generic 0
%endif

%if %{suse}
  %define generic 0
%endif
### END Distro Definitions

%define		name wmclockmon
%define		version 0.8.1
%define		release 6%{?dist}

Summary:	digital clock with 7 different styles in either LCD or LED style
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		AfterStep/Applets
URL:		http://tnemeth.free.fr/projets/dockapps.html
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glib
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXi
Requires:	libXpm
BuildRequires:	glib-devel
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXpm-devel

%if %{mdk}
Requires:	libgtk+1.2
Buildrequires:	libgtk+1.2-devel
%endif

%if %{fedora}
Requires:	gtk+
Requires:	gdk-pixbuf
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel
%endif

%description
wmclockmon is a nice digital clock with 7 different styles in either
LCD or LED style; uses locales to display weekday and month names.
It also features the internet time.
Includes wmclockmon-cal, a calendar display and wmclockmon-config,
a configuration tool for the package.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wmclockmon/

rm -rf styles/Makefile*

install -m 644 styles/* $RPM_BUILD_ROOT%{_datadir}/wmclockmon/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}*
%{_mandir}/man1/*
%dir %{_datadir}/wmclockmon
%{_datadir}/wmclockmon/*
%doc doc/sample*.wmclockmonrc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO

%changelog
* Wed Oct 19 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-6
- cleanup.

* Fri Jun 15 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-5
- added require for gtk+-devel, gtk+.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-2
- changed prefix path to /usr.

* Sun Apr 10 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-1
- Updated to 0.8.1.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-2
- Changed styles dir to /usr/X11R6/share from /usr/share.

* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-1
- Initial build.

