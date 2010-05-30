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

%define name trayer
%define version 1.0
%define release 5%{?dist}

Summary: A lightweight GTK2-based systray for UNIX desktop
Name: %name
Version: %version
Release: %release
License: GPL
Group: User Interface/Desktops
URL: http://fvwm-crystal.org/
Source0: http://download.gna.org/fvwm-crystal/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-%{version}-Makefile.common.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libXmu-devel

%description
A lightweight GTK2-based systray for UNIX desktop.

%prep
%setup -q
%patch0

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 trayer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc CREDITS COPYING CHANGELOG README

%changelog
* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.0-5
- improved links in Makefile.common patch file.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 1.0-4
- added build requirement for libXmu-devel.

* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.0-3
- added patch for gtk issues (thanks Team Debian).

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.0-2
- added distro info to release.

* Mon Jun 26 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build.
