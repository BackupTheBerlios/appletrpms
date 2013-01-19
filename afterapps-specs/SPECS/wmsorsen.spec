%define name	wmsorsen
%define version	0.10.1
%define release	3%{?dist}

Summary:	dockapp for window maker for displaying hardware sensor values.
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.boomerangsworld.de/cms/dockapps/wmsorsen/index?lang=en
Source0:	http://www.boomerangsworld.de/cms/dockapps/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libgcc
Requires:	libstdc++
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	lm_sensors >= 3.0.0,
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	lm_sensors-devel >= 3.0.0

%description
wmsorsen is a dockapp for window maker (and similar window 
managers supporting dockapps) for display hardware sensor values.

It's based on wmsensormon (http://wmsensormon.sourceforge.net).

%prep
%setup -q
%patch0

%build
cd wmsorsen

make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

cd wmsorsen

make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/wmsorsen
%doc CHANGELOG COPYING README wmsorsen/wmsorsenrc

%changelog
* Fri Jan 18 2013 J. Krebs <rpm_speedy@yahoo.com> - 0.10.1-3
- updated tarball link.

* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.10.1-2
- updated spec file.

* Tue Jun 22 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.10.1-1
- new version.

* Wed Nov 18 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.10.0-1
- Initial build.
