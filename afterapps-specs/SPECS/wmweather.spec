%define		name wmweather
%define		version 2.4.5
%define		release 2%{?dist}

Summary:	wmweather is a dockapp that displays the current weather
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://people.debian.org/~godisch/wmweather/
Source0:	http://ftp.de.debian.org/debian/pool/main/w/wmweather/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	curl-devel
Requires:	curl
Provides:	wmWeather
Obsoletes:	wmWeather

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
./configure --prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sysconfdir=%{_sysconfdir} \
	--without-xmessage \
	--mandir=%{_mandir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

cd src

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING README src/wmweather.conf
%{_bindir}/%{name}
%{_bindir}/wmWeather
%{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/wmWeather.*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.4.5-2
- updated spec file.

* Fri Aug 28 2009 J. Krebs <rpm_speedy@yahoo.com> - 2.4.5-1
- new version.

* Thu Aug 20 2009 J. Krebs <rpm_speedy@yahoo.com> - 2.4.4-2
- Updated URLs.

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
