### BEGIN Distro Defines
%define mdk  %(if [ -e /etc/mandrake-release ]; then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1

%if %{mdk}
  %define generic 0
%endif
%if %{fedora}
  %define generic 0
%endif
%if %{suse}
  %define generic 0
%endif
### END Distro Definitions

%define prefix	/usr
%define version 0.6.1
%define release 3

%if %{mdk}
%define name	libdockapp0
%endif
%if %{fedora}
%define name	libdockapp
%endif
%if %{suse}
%define name	libdockapp
%endif
%if %{generic}
%define name	libdockapp
%endif

Summary:	DockApp Making Standard Library
Name:		%name
Version:	%version
Release:	%release
License:	CustomOpenSource
Group:		X11/Libraries
Source0:	libdockapp-%{version}.tar.bz2
URL:		http://solfertje.student.utwente.nl/~dalroi/libdockapp/
BuildRequires:	autoconf automake libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdk}
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
	--without-examples \
	--without-fonts
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{prefix}/lib/libdockapp.a
rm -rf $RPM_BUILD_ROOT%{prefix}/X11R6/lib/X11/fonts/dockapp/*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{prefix}/lib/lib*.so.*
#%{prefix}/lib/X11/fonts/dockapp/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{prefix}/lib/lib*.so
%attr(755,root,root) %{prefix}/lib/lib*.la
%{prefix}/include/*

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> 0.6.1-3
- changed prefix path to /usr.

* Mon Jan 02 2006 J. Krebs <rpm_speedy@yahoo.com> 0.6.1-2
- added improved build clean-up.

* Mon Jul 18 2005 J. Krebs <rpm_speedy@yahoo.com> 0.6.1-1
- new version.

* Sat Jun 25 2005 J. Krebs <rpm_speedy@yahoo.com> 0.6.0-1
- initial build.
