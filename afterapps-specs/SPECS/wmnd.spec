%define name wmnd
%define version 0.4.12
%define release 2%{?dist}

Summary: wmnd is a network monitoring dockapp
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.yuv.info/wmnd/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/info/*
rm -rf $RPM_BUILD_ROOT%{_datadir}/wmndrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO examples/wmndrc


%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.12-2
- added distro info to release.

* Sun May 28 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.12-1
- changed prefix path to /usr.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.11-2
- changed prefix path to /usr.

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.11-1
- Initial build.
