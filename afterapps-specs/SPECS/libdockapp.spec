%define generic 1
%define fedora 0
%{?_with_fedora:%define fedora 1}
%define mandrake 0
%{?_with_mandrake:%define mandrake 1}
%if %{fedora}
   %define generic 0
%endif
%if %{mandrake}
   %define generic 0
%endif

%define prefix	/usr/X11R6
%define version 0.6.1
%define release 1

%if %{mandrake}
%define name	libdockapp0
%endif

%if %{fedora}
%define name	libdockapp
%endif

Summary:	DockApp Making Standard Library
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		X11/Libraries
Source0:	libdockapp-%{version}.tar.bz2
URL:		http://solfertje.student.utwente.nl/~dalroi/libdockapp/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %{mandrake}
Conflicts:	libdockapp
Provides:	libdockapp0 libdockapp.so.2
%endif

%if %{fedora}
Conflicts:	libdockapp0
Provides:	libdockapp libdockapp.so.2
%endif

%description
DockApp Making Standard Library.

%package devel
Summary:	Header files etc to develop DockApps
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc to develop DockApps.

%prep
%setup -q -n dockapp-%{version}

%build
./configure --prefix=%{prefix} \
	--with-x \
	--without-examples
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{prefix}/lib/libdockapp.a

%clean

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{prefix}/lib/lib*.so.*
%{prefix}/lib/X11/fonts/dockapp/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{prefix}/lib/lib*.so
%attr(755,root,root) %{prefix}/lib/lib*.la
%{prefix}/include/*

%changelog
* Mon Jul 18 2005 J. Krebs <rpm_speedy@yahoo.com> 0.6.1-1
- new version.

* Sat Jun 25 2005 J. Krebs <rpm_speedy@yahoo.com> 0.6.0-1
- initial build.
