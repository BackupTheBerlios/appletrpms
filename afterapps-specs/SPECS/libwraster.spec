%define prefix /usr

Summary: 	wraster libraries used in WindowMaker.
Name: 		libwraster
Version:	0.80.2
Release:	2
License:	GPL
Group: 		User Interface/Desktops
URL: 		http://www.windowmaker.info/
Source: 	http://open-systems.ufl.edu/mirrors/gentoo/distfiles/WindowMaker-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib
mkdir -p $RPM_BUILD_ROOT%{prefix}/include

ln -s ./libwraster.so.2.2.0 $RPM_BUILD_ROOT%{prefix}/lib/libwraster.so
ln -s ./libwraster.so.2.2.0 $RPM_BUILD_ROOT%{prefix}/lib/libwraster.so.2

install -m 644 wrlib/.libs/libwraster.a $RPM_BUILD_ROOT%{prefix}/lib/
install -m 644 wrlib/libwraster.la $RPM_BUILD_ROOT%{prefix}/lib/
install -m 755 wrlib/.libs/libwraster.so.2.2.0 $RPM_BUILD_ROOT%{prefix}/lib/
install -m 644 wrlib/wraster.h $RPM_BUILD_ROOT%{prefix}/include/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/include/*.h
%prefix/lib/libw*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.80.2-2
- Updated Source path and URL.

* Mon Mar 07 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.80.2-1
- initial build
