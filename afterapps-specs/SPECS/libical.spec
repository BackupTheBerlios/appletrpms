%define	name	libical
%define	version	0.24.RC4
%define release 1
%define	prefix	/usr

Summary:	An implementation of basic iCAL protocols
Name:		%{name}
Version:	%{version}
Release:	%{release}
Copyright:	MPL
Group:		Development/Libraries/C and C++
URL:		http://softwarestudio.org/libical/
Source0:	%name-%version.tar.gz
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
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/libical/scripts/
install -m 644 scripts/*.pl $RPM_BUILD_ROOT%{prefix}/share/libical/scripts/
rm -rf $RPM_BUILD_ROOT%{prefix}/lib/libLibicalWrap*
rm -rf doc/Makefil*
rm -rf examples/Makefil*
rm -rf $RPM_BUILD_ROOT%{prefix}/share/doc/%{name}-%{version}/scripts/

%post
%run_ldconfig

%postun
%run_ldconfig

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

%changelog
* Fri May 20 2005 - J. Krebs <rpm_speedy@yahoo.com> 0.24.RC4-1
- initial build.
