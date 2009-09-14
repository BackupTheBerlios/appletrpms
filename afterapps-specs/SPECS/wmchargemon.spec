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

%define name	wmchargemon
%define version 0.3
%define release 3%{?dist}

Summary:	displays ACPI battery level and power status
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		AfterStep/Applets
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
URL:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
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

make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 wmchargemon $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog INSTALL README
%{_bindir}/*

%changelog
* Sun Sep 13 2009 J. Krebs <rpm_speedy@yahoo.com> 0.3-3
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> 0.3-2
- added distro info to release.

* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> 0.3-1
- new version.

* Wed Oct 25 2006 J. Krebs <rpm_speedy@yahoo.com> 0.2-2
- added build requires for libdockapp.

* Sat Sep 23 2006 J. Krebs <rpm_speedy@yahoo.com> 0.2-1
- initial build.
