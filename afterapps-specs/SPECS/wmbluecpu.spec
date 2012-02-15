%define		name wmbluecpu
%define		version 0.9
%define		release 3%{?dist}

Summary:	dockapp cpu monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/167
Source0:	http://dockapps.windowmaker.org/download.php/id/770/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-Makefile.patch
Patch1:		%{name}-%{version}-cpu_linux.c.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXft
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
Requires:	libXft-devel
BuildRequires:	libXpm-devel
Obsoletes:	WMBlueCPU

%description
WMBlueCPU is a cpu monitor. It runs either as a dockapp or
in a normal window. It displays the number of the cpu being
monitored in the top left corner, the cpu usage in the top
right corner, and a usage history chart at the bottom.

%prep
%setup -q -n wmbluecpu
%patch0
%patch1

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 wmbluecpu $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmbluecpu.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS COPYING ChangeLog README THANKS

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.9-3
- shifted URLs to http://dockapps.windowmaker.org.

* Fri Oct 28 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- added patch for SMP processors to default to CPU0.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- new version. changed URL info to dockapps.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-5
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-4
- Updated Source path. Sheepmakers site is invalid.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1
- Initial build.



