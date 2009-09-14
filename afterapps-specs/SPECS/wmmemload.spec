%define name wmmemload
%define version 0.1.6
%define release 5%{?dist}

Summary: memory monitor dockapp which displays free memory and swap space
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: https://sourceforge.net/projects/freshmeat_wmmemload/
Source0: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
wmmemload is a simple dockapp for WindowMaker on X Windows that
displays memory and swap space usage. It is very heavily based
on WMMemMon and WMCPULoad by Seiichi SATO. 

%prep
%setup -q -n %{name}-%{version}

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
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS


%changelog
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



