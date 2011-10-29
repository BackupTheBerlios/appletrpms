%define name	wmnd
%define version	0.4.16
%define release	2%{?dist}

Summary:	wmnd is a network monitoring dockapp
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.thregr.org/~wavexx/software/wmnd/
Source0:	http://www.thregr.org/~wavexx/software/wmnd/releases/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-make-byte-packet-counters-64-bit.patch
Patch1:		%{name}-%{version}-ld.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
WMND (WindowMaker Network Devices) is a network monitoring
dockapp for Window Maker (and compatibles) for many operative systems.
Improved and based on WMiFS 1.3b, the version 0.2 of WMND is almost
totally written by Timecop, given the optimization and flexibility and
now consumes less cpu than wmmon. Version >= 0.3 WMND is now
maintained by wave++, which added new display modes and several new
drivers. Enjoy!

%prep
%setup -q
%patch0
%patch1

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/wmndrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO examples/wmndrc
%{_bindir}/wmnd
%{_mandir}/man1/wmnd.*

%changelog
* Wed Oct 19 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.4.16-2
- added requires and buildrequires, added packet counter & ld patches.

* Tue Jun 21 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.4.16-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.12-2
- added distro info to release.

* Sun May 28 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.12-1
- changed prefix path to /usr.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.11-2
- changed prefix path to /usr.

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.11-1
- Initial build.
