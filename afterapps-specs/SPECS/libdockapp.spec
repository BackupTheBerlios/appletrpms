### BEGIN Distro Defines
### mdk, fedora, suse & generic are distros
### mandriva, fedoragcc4, and susegcc4 define gcc 4.0 compilers
%define mdk  %(if [ -e /etc/mandrake-release -o -e /etc/mandriva-release]; then echo 1;\
 else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define mandriva  %(if [ -e /etc/mandriva-release ]; then echo 1; else echo 0; fi;)
%{?_with_mandriva:   %{expand: %%global mandriva 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1

%if %{fedora}
  %define generic 0
%endif

%if %{fedora}
  %define generic 0
  %define fcgcctest $(grep release /etc/fedora-release | cut -d ' ' -f4)
  %define fedoragcc4 %(if [ %fcgcctest -ge 4 ]; then echo 1; else echo 0; fi;)
  %{?_with_fedoragcc4:   %{expand: %%global fedoragcc4 1}}
%endif

%if %{suse}
  %define generic 0
  %define susegcctest $(grep VERSION /etc/SuSE-release | cut -d ' ' -f3)
  %define susegcc4 %(if [ %susegcctest -ge 10.0 ]; then echo 1; else echo 0; fi;)
  %{?_with_susegcc4:   %{expand: %%global susegcc4 1}}
%endif
### END Distro Definitions

%define prefix	/usr/X11R6
%define version 0.6.1
%define release 2

%if %{mdk}
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
	--without-examples
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{prefix}/lib/libdockapp.a

%clean
rm -rf $RPM_BUILD_ROOT

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
* Mon Jan 02 2006 J. Krebs <rpm_speedy@yahoo.com> 0.6.1-2
- added improved build clean-up.

* Mon Jul 18 2005 J. Krebs <rpm_speedy@yahoo.com> 0.6.1-1
- new version.

* Sat Jun 25 2005 J. Krebs <rpm_speedy@yahoo.com> 0.6.0-1
- initial build.
