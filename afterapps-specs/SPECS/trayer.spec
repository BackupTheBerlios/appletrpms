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

%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name trayer
%define version 1.0
%define release 1

Summary: A lightweight GTK2-based systray for UNIX desktop.
Name: %name
Version: %version
Release: %release
License: GPL
Group: User Interface/Desktops
URL: http://fvwm-crystal.org/
Source0: http://download.gna.org/fvwm-crystal/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A lightweight GTK2-based systray for UNIX desktop.

%prep
%setup -q

%build
make PREFIX=%{__prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 trayer $RPM_BUILD_ROOT%{_bindir}

#@mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
#install -m 644 README $RPM_BUILD_ROOT%{_mandir}/man1/trayer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
#%{_mandir}/*
%doc CREDITS COPYING CHANGELOG README

%changelog
* Mon Jun 26 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build.
