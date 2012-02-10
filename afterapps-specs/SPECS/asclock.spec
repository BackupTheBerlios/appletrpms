%define		name asclock
%define		version 2.0.12
%define		release 8%{?dist}

Summary:	Clock Applet
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=asclock/data
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.config
Patch0:		%{name}-%{version}.xpm.path.patch
Patch1:		%{name}-%{version}-gcc41.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	imake
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
AfterStep clock applet

%prep
%setup -q
%patch0
%patch1

%build
mv configure configure.old
cp %{SOURCE1} configure
./configure
make

%install
rm -rf $RPM_BUILD_ROOT

make BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    DOCDIR=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version} \
    install install.man

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a themes/* $RPM_BUILD_ROOT%{_datadir}/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/Freeamp/Makefile
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/Freeamp/Makefile.am
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/Freeamp/Makefile.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README README.THEMES TODO
%{_bindir}/asclock
%{_mandir}/man1/asclock.*
%{_datadir}/%{name}/Freeamp/beats.xpm
%{_datadir}/%{name}/Freeamp/clock.xpm
%{_datadir}/%{name}/Freeamp/config
%{_datadir}/%{name}/Freeamp/date.xpm
%{_datadir}/%{name}/Freeamp/hour.xpm
%{_datadir}/%{name}/Freeamp/led.xpm
%{_datadir}/%{name}/Freeamp/minute.xpm
%{_datadir}/%{name}/Freeamp/month.xpm
%{_datadir}/%{name}/Freeamp/old.clock.xpm
%{_datadir}/%{name}/Freeamp/second.xpm
%{_datadir}/%{name}/Freeamp/weekday.xpm
%{_datadir}/%{name}/Newstone/beats.xpm
%{_datadir}/%{name}/Newstone/clock.xpm
%{_datadir}/%{name}/Newstone/config
%{_datadir}/%{name}/Newstone/date.xpm
%{_datadir}/%{name}/Newstone/hour.xpm
%{_datadir}/%{name}/Newstone/led.xpm
%{_datadir}/%{name}/Newstone/minute.xpm
%{_datadir}/%{name}/Newstone/month.xpm
%{_datadir}/%{name}/Newstone/second.xpm
%{_datadir}/%{name}/Newstone/weekday.xpm
%{_datadir}/%{name}/Orb/beats.xpm
%{_datadir}/%{name}/Orb/clock.xpm
%{_datadir}/%{name}/Orb/config
%{_datadir}/%{name}/Orb/date.xpm
%{_datadir}/%{name}/Orb/hour.xpm
%{_datadir}/%{name}/Orb/led.xpm
%{_datadir}/%{name}/Orb/minute.xpm
%{_datadir}/%{name}/Orb/month.xpm
%{_datadir}/%{name}/Orb/second.xpm
%{_datadir}/%{name}/Orb/weekday.xpm
%{_datadir}/%{name}/Stone/beats.xpm
%{_datadir}/%{name}/Stone/clock.xpm
%{_datadir}/%{name}/Stone/config
%{_datadir}/%{name}/Stone/date.xpm
%{_datadir}/%{name}/Stone/hour.xpm
%{_datadir}/%{name}/Stone/led.xpm
%{_datadir}/%{name}/Stone/minute.xpm
%{_datadir}/%{name}/Stone/month.xpm
%{_datadir}/%{name}/Stone/second.xpm
%{_datadir}/%{name}/Stone/weekday.xpm
%{_datadir}/%{name}/beats/beats.xpm
%{_datadir}/%{name}/beats/classic
%{_datadir}/%{name}/beats/clock.xpm
%{_datadir}/%{name}/beats/config
%{_datadir}/%{name}/beats/date.xpm
%{_datadir}/%{name}/beats/hour.xpm
%{_datadir}/%{name}/beats/led.xpm
%{_datadir}/%{name}/beats/minute.xpm
%{_datadir}/%{name}/beats/month.xpm
%{_datadir}/%{name}/beats/second.xpm
%{_datadir}/%{name}/beats/weekday.xpm
%{_datadir}/%{name}/classic/beats.xpm
%{_datadir}/%{name}/classic/classic
%{_datadir}/%{name}/classic/clock.xpm
%{_datadir}/%{name}/classic/config
%{_datadir}/%{name}/classic/date.xpm
%{_datadir}/%{name}/classic/hour.xpm
%{_datadir}/%{name}/classic/led.xpm
%{_datadir}/%{name}/classic/minute.xpm
%{_datadir}/%{name}/classic/month.xpm
%{_datadir}/%{name}/classic/second.xpm
%{_datadir}/%{name}/classic/weekday.xpm
%{_datadir}/%{name}/penguin/clock.xpm
%{_datadir}/%{name}/penguin/config
%{_datadir}/%{name}/penguin/date.xpm
%{_datadir}/%{name}/penguin/led.xpm
%{_datadir}/%{name}/penguin/month.xpm
%{_datadir}/%{name}/shaped/beats.xpm
%{_datadir}/%{name}/shaped/classic
%{_datadir}/%{name}/shaped/clock.xpm
%{_datadir}/%{name}/shaped/config
%{_datadir}/%{name}/shaped/date.xpm
%{_datadir}/%{name}/shaped/hour.xpm
%{_datadir}/%{name}/shaped/led.xpm
%{_datadir}/%{name}/shaped/minute.xpm
%{_datadir}/%{name}/shaped/month.xpm
%{_datadir}/%{name}/shaped/second.xpm
%{_datadir}/%{name}/shaped/weekday.xpm

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-8
- removed some .old files from package.

* Sun May 30 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-7
- some spec file cleanup.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-6
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-4
- changed prefix path to /usr.

* Tue Jul 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.0.12-3
- Added patches for gcc-4.0 and theme path.

* Sat Aug 30 2003 Sean Dague <sean@dague.net> - 2.0.12-2
- Add in theme support

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 
- Initial build.


