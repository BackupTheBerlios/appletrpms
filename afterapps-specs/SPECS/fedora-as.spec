%define	name fedora-as
%define	version	1.1
%define release 1%{?dist}

Summary:	AfterStep Applets Fedora release file and package configuration
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		System Environment/Base
URL:		ftp://ftp.afterstep.org/stable/rpms/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description

AfterStep Applets Fedora release file. This package also contains yum
configuration to use the AfterStep Fedora-provided rpm packages.

%prep

%setup -q

cp fedora-as.repo.txt %{name}.repo

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d/
install -m 644 fedora-as.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
/etc/yum.repos.d/fedora-as.repo

%changelog
* Fri Apr 29 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.1-1
- added SRPMS setup for Fedora 14 and later.

* Sat Feb 16 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build
