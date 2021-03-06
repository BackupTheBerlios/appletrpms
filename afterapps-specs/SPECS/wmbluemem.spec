%define		name wmbluemem
%define		version 0.12
%define		release 2%{?dist}

Summary:	dockapp memory monitoring program
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/165
Source0:	http://dockapps.windowmaker.org/download.php/id/771/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXft
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXft-devel
BuildRequires:	libXpm-devel
Obsoletes:	WMBlueMem wmmemfree

%description
WMBlueMem is a memory monitoring program. It runs either as a
dockapp or a normal window. On the top the physical memory
usage is displayed and on the bottom the swap space usage is
displayed.

%prep
%setup -q -n wmbluemem
%patch0

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README THANKS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.12-2
- shifted URLs to http://dockapps.windowmaker.org.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.12-1
- new version. changed URL info to dockapps.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-5
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-4
- Updated Source path. Sheepmakers site is invalid.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Sat Oct 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.



