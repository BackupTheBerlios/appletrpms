%define		name wminet
%define		version 3.0.0
%define		release 5%{?dist}

Summary:	dockapp for monitoring internet connections to/from your computer
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.swanson.ukfsn.org/#wminet
Source0:	http://www.swanson.ukfsn.org/wmdock/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
Very useful dock app for monitoring internet connections to and
from your computer. The number of connections can be filtered
based on local and remote addresses and ports, on either tcp or
udp. It can also display hostname and number of processes.

Includes both standard and LCD-style displays.

This new version uses a lot less CPU and allows greater
configuration. The ability to monitor httpd and ftpd processes,
nfs mounts and lpd queues has been removed from the original. 

%prep
%setup -q

%build
./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README wminetrc
%{_bindir}/wminet

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-5
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-2
- changed prefix path to /usr.

* Fri Mar 25 2005 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-1
- Initial build.
