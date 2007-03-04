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
%define version 0.3
%define release 1
%define name	wmchargemon

Summary:	displays ACPI battery level and power status
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		AfterStep/Applets
Source0:	http://dockapps.org/download.php/id/715/%{name}-%{version}.tar.gz
URL:		http://dockapps.org/file.php/id/319
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if %{mdk}
Requires: libdockapp0
BuildRequires: libdockapp0-devel
%endif

%if %{fedora}
Requires: libdockapp
BuildRequires: libdockapp-devel
%endif

%description
WMChargemon is a simple dockapp showing, in a clear way, the
battery level and the power status of your ACPI-driven laptop.
Low and critical battery levels (on which the applet changes
its color) can be set.

%prep
%setup -q

%build

make PREFIX=%{prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin

install -s -m 755 wmchargemon $RPM_BUILD_ROOT%{prefix}/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog INSTALL README
%{_bindir}/*

%changelog
* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> 0.3-1
- new version.

* Wed Oct 25 2006 J. Krebs <rpm_speedy@yahoo.com> 0.2-2
- added build requires for libdockapp.

* Sat Sep 23 2006 J. Krebs <rpm_speedy@yahoo.com> 0.2-1
- initial build.
