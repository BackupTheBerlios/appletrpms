%define		name wmppp
%define		version 1.3.0
%define		release 5%{?dist}

Summary:	wmppp provides a PPP activator and network load monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/net.html
Source0:	http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-hispeed.patch
Patch1:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	ppp
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
WMPPP features all things the standard pppd offers and gives
you some nice additional features too...

        * Integrated online timer;
        * Integrated modem RX/TX LED's;
		* Integrated WMPPP status LED; 
        * Integrated autoscaling PPP transfer statistics;
		* Integrated CARRIER/CONNECT display;
		* Integrated bytes/second Speed-O-Meter;
		* Automatic detection of active ppp interfaces;
		* User definable scripts for the V and X buttons and
  		  also for 'ifdown' which are read from ~/.wmppprc;
		* 'force' option in /etc/ppp/.wmppprc for sites
  		  where users are not allowed to mess with pppd;
		* Several commandline options (try '-h' for help);

WMPPP is being developped on DEC Alpha machines running Linux
(RedHat-5.0 and RedHat-5.1), but WMPPP is also intensively 
tested on x86 and m68k Linux machines...

%prep
%setup -q -n wmppp.app
%patch0
%patch1

%build
cd wmppp

make %{?_smp_mflags} \
	PREFIX=%{_prefix} \
	SYSCONFDIR=%{_sysconfdir} all

%install
rm -rf $RPM_BUILD_ROOT

cd wmppp

make PREFIX=%{_prefix} \
	SYSCONFDIR=%{_sysconfdir} \
	DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc BUGS CHANGES COPYING HINTS README TODO wmppp/*.wmppprc wmppp/example-scripts
%{_bindir}/wmppp
%{_sysconfdir}/ppp/getmodemspeed
%{_sysconfdir}/wmppprc

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-5
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-2
- changed prefix path to /usr.

* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.3.0-1
- Initial build.
