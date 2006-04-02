%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmweather
%define version 2.4.3
%define release 2

Summary: wmweather is a dockapp that displays the current weather.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.godisch.de/debian/wmweather/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
./configure --prefix=%{__prefix} --sysconfdir=/etc --without-xmessage --mandir=%{_mandir}
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
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-2
- changed prefix path to /usr.

* Sat Jan 06 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-1
- Initial build.
