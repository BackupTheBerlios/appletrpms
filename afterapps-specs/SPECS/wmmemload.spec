%define		name wmmemload
%define		version 0.1.6
%define		release 7%{?dist}

Summary:	memory monitor dockapp which displays free memory and swap space
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		https://sourceforge.net/projects/freshmeat_wmmemload/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-man.patch
Patch1:		%{name}-%{version}-kfbsd-configure.patch
Patch2:		%{name}-%{version}-kernel-3.0.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
wmmemload is a simple dockapp for WindowMaker on X Windows that
displays memory and swap space usage. It is very heavily based
on WMMemMon and WMCPULoad by Seiichi SATO. 

%prep
%setup -q -n %{name}-%{version}
%patch0
%patch1
%patch2

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 src/wmmemload $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog THANKS

%changelog
* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-7
- added kernel 3.0, man page, kfsbd patches from debian.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-6
- changed URL info to dockapps.org.

* Fri Aug 07 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-5
- Updated URLs.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-2
- changed prefix path to /usr.

* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-1
- Initial build.



