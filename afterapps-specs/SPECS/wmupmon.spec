%define		name wmupmon
%define		version 0.1.3
%define		release 7%{?dist}

Summary:	DockApp that displays your system uptime in realtime
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/188
Source0:	http://dockapps.windowmaker.org/download.php/id/547/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-arraysize.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
DockApp that displays your system uptime in realtime.

%prep
%setup -q
%patch0

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog THANKS README COPYING
%{_bindir}/wmupmon
%{_mandir}/man1/wmupmon.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-7
- shifted URLs to http://dockapps.windowmaker.org.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-6
- changed URL info to dockapps.org.

* Sat Apr 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-5
- Website is no longer available. Moved links to ftp.afterstep.org.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-2
- changed prefix path to /usr.

* Wed Mar 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.3-1
- Initial build.

