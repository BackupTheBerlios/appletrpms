%define		name wmix
%define		version 3.2
%define		release 6%{?dist}

Summary:	dockapp mixer utilizing the OSS mixer API
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.dockapps.org/file.php/id/58
Source0:	http://www.dockapps.org/download.php/id/528/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	glibc
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	glibc-devel

%description
- This is a complete dockapp mixer utilizing the OSS mixer API
- Has a nice On-Screen-Display to visualize current volume levels
- Can adjust main volume, balance, recording status, and
  mute/unmute channels
- Supports mousewheel to adjust the volume settings
- Supports user specified signals to adjust the volume remotely
- User configuration file can be used to set options

%prep
%setup -q

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 wmix $RPM_BUILD_ROOT%{_bindir}
install -m 644 wmix.1x.gz $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS BUGS COPYING NEWS README sample.wmixrc

%changelog
* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 3.2-6
- changed URL info to dockapps.org.

* Sun Sep 13 2009 J. Krebs <rpm_speedy@yahoo.com> - 3.2-5
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 3.2-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.2-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.2-2
- changed prefix path to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 3.2-1
- Initial build.
