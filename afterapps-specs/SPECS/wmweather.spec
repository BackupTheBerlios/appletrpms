%define prefix /usr/X11R6
%define name wmweather
%define version 2.4.3
%define release 1

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
./configure --prefix=%prefix --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT

cd src
make install DESTDIR=$RPM_BUILD_ROOT

#rm -rf $RPM_BUILD_ROOT/etc/wmweather.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
/etc/*
%prefix/man/man1/*
%doc CHANGES COPYING README src/wmweather.conf

%changelog
* Sat Jan 06 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.4.3-1
- Initial build.
