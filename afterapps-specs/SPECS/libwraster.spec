%define name	libwraster
%define version	0.80.2
%define release	4%{?dist}

Summary: 	wraster libraries used in WindowMaker
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group: 		User Interface/Desktops
URL: 		http://www.windowmaker.info/
Source: 	http://www.windowmaker.info/pub/source/release/archive/WindowMaker-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libpng-devel libjpeg-devel libungif-devel 
BuildRequires:	libtiff-devel zlib-devel gettext
Conflicts:	WindowMaker WindowMaker-libs WindowMaker-devel
Provides:	libwraster libwraster.so libwraster.so.2

%description
This package contains the wraster libraries used in WindowMaker. The
primary purpose of this package is to allow the installation of these
libraries without the full installation of WindowMaker. Many WindowMaker
applets and applications can be used by other window managers (AfterStep,
IceWM, etc.) with these libraries.  This package allows installation of
these programs independent of WindowMaker.

%prep
%setup -q -n WindowMaker-%{version}

%build
%configure --prefix=%{_prefix} --libdir=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}

ln -s ./libwraster.so.2.2.0 $RPM_BUILD_ROOT%{_libdir}/libwraster.so
ln -s ./libwraster.so.2.2.0 $RPM_BUILD_ROOT%{_libdir}/libwraster.so.2

install -m 644 wrlib/.libs/libwraster.a $RPM_BUILD_ROOT%{_libdir}/
install -m 644 wrlib/libwraster.la $RPM_BUILD_ROOT%{_libdir}/
install -m 755 wrlib/.libs/libwraster.so.2.2.0 $RPM_BUILD_ROOT%{_libdir}/
install -m 644 wrlib/wraster.h $RPM_BUILD_ROOT%{_includedir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/libw*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Fri May 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.80.2-4
- added rpm macro libdir to configure.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.80.2-3
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.80.2-2
- Updated Source path and URL.

* Mon Mar 07 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.80.2-1
- initial build
