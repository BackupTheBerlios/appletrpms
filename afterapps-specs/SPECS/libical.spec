%define	name	libical
%define	version	0.43
%define release 1%{?dist}

Summary:	An implementation of basic iCAL protocols
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Dual LGPLv2+ and MPLv1.0
Group:		Development/Libraries/C and C++
URL:		http://softwarestudio.org/libical/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/freeassociation/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	byacc flex bison gcc-c++

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package devel
Summary:	libical include files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
libical include files.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--enable-shared \
	--libdir=%{_libdir}

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -m 644 scripts/*.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TEST THANKS TODO doc/AddingOrModifyingComponents.txt doc/UsingLibical.txt
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_includedir}/%{name}/*.h
%{_datadir}/libical/scripts/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.43-1
- new version.

* Sun May 25 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.31-1
- new version.

* Thu Oct 11 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.27-1
- new version.

* Fri May 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.24.RC4-6
- added rpm macro libdir to configure.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.24.RC4-5
- added distro info to release, added devel package.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.24.RC4-4
- Updated Source path.

* Fri Jun 10 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-3
- replaced "copyright" with "license".

* Fri Jun 03 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-2
- .spec script cleanup.

* Fri May 20 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-1
- initial build.
