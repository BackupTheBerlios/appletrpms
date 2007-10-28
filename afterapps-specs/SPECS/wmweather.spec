%define name wmweather
%define version 2.4.4
%define release 1%{?dist}

Summary: wmweather is a dockapp that displays the current weather
Name: %name
Version: %version
Release: %release
License: GPLv2+
Group: AfterStep/Applets
URL: http://www.godisch.de/debian/wmweather/
Source0: http://www.godisch.de/debian/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: curl-devel
Requires: curl
Provides: wmWeather
Obsoletes: wmWeather

%description
wmweather provides a monitor on a 64x64 mini window that displays
the current weather. The weather reports are received from NOAA's
National Weather Service (http://weather.noaa.gov), which is the
same source that pilots use. wmweather is designed to work with the
WindowMaker dock, but will work with other window managers as well.

%prep
%setup -q

%build
cd src
./configure --prefix=%{_prefix} --sysconfdir=/etc --without-xmessage --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

cd src
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}*
/etc/*
%{_mandir}/man1/*
%doc CHANGES COPYING README src/wmweather.conf

%changelog
* Fri Sep 28 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.4.4-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-2
- changed prefix path to /usr.

* Sat Jan 06 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-1
- Initial build.
