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
%define version 0.1.1
%define release 1
%define name	wmnethru

Summary:	Network Throughput and System Utilization Monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		AfterStep/Applets
Source0:	http://dockapps.org/download.php/id/693/%{name}-%{version}.tar.gz
URL:		http://dockapps.org/file.php/id/315
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %{mdk}
Requires: libdockapp0
BuildRequires: libdockapp0-devel
%endif

%if %{fedora}
Requires: libdockapp
BuildRequires: libdockapp-devel
%endif

%description
Network Throughput and System Utilization Monitor.
Four lines are periodically updated. The first line is
the time since the last check point. The second, third
and fourth lines are the average CPU utilization, the
total outgoing bytes through the specified network
device, and the total incoming bytes through the same
device, respectively, during the period indicated by
the first line.

To reset the statistics (i.e., to set the check point
to the current time), click the right mouse button. To
update the statistics immediately, click the left
mouse button.

%prep
%setup -q -n %{name}

%build

make DESTDIR=%{prefix}/bin                     \
	LIBDIR=-L%{prefix}/lib                   \
	INCDIR=-I%{prefix}/include/X11

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin

install -s -m 755 wmnethru $RPM_BUILD_ROOT%{prefix}/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{prefix}/bin/*

%changelog
* Sat Sep 23 2006 J. Krebs <rpm_speedy@yahoo.com> 0.1.1-1
- initial build.
