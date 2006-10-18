%define	name	libical
%define	version	0.24.RC4
%define release 4
%define	prefix	/usr

Summary:	An implementation of basic iCAL protocols
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Development/Libraries/C and C++
URL:		http://softwarestudio.org/libical/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/freeassociation/%name-%version.tar.gz
Patch0:		%name.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%prep
%setup -q -n %{name}-0.24
%patch0

%build
autoreconf -f -i
CFLAGS="$RPM_OPT_FLAGS" \
CXXFLAGS="$RPM_OPT_FLAGS" \
  ./configure \
     --prefix=%{prefix} \
     --exec-prefix=%{prefix} \
     --with-devel \
     --enable-python
make

%install
make install DESTDIR=%{buildroot}
rm -rf examples/.deps/
rm -rf examples/.libs
rm examples/*.o
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/%{name}/scripts/
install -m 644 scripts/*.pl $RPM_BUILD_ROOT%{prefix}/share/%{name}/scripts/
rm -rf doc/Makefil*
rm -rf examples/Makefil*
rm -rf $RPM_BUILD_ROOT%{prefix}/share/doc/%{name}-%{version}/scripts/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TEST THANKS TODO doc examples
%{prefix}/lib/*.so.*
%{prefix}/lib/*.*a
%{prefix}/lib/*.so
%{prefix}/include/*.h
%dir %{prefix}/share/libical
%{prefix}/share/libical/zoneinfo/*
%{prefix}/share/libical/scripts/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.24.RC4-4
- Updated Source path.

* Fri Jun 10 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-3
- replaced "copyright" with "license".

* Fri Jun 03 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-2
- .spec script cleanup.

* Fri May 20 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-1
- initial build.
