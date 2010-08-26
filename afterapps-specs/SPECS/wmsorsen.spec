%define name	wmsorsen
%define version	0.10.1
%define release	1%{?dist}

Summary:	dockapp for window maker for displaying hardware sensor values.
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.boomerangsworld.de/cms/dockapps/wmsorsen/index?lang=en
Source0:	http://www.boomerangsworld.de/cms/dockapps/wmsorsen/downloads/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	lm_sensors-devel >= 3.0.0, libXpm-devel libXext-devel libstdc++-devel
Requires:	lm_sensors >= 3.0.0, libXpm libXext libstdc++

%description
wmsorsen is a dockapp for window maker (and similar window managers supporting
dockapps) for display hardware sensor values.

It's based on wmsensormon (http://wmsensormon.sourceforge.net).

%prep
%setup -q

%build
cd wmsorsen

make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 wmsorsen/wmsorsen $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc CHANGELOG COPYING INSTALL README wmsorsen/wmsorsenrc

%changelog
* Tue Jun 22 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.10.1-1
- new version.

* Wed Nov 18 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.10.0-1
- Initial build.
