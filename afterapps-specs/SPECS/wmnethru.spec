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

%define		name wmnethru
%define		version 0.1.1
%define		release 4%{?dist}

Summary:	Network Throughput and System Utilization Monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
Source0:	http://www.dockapps.org/download.php/id/693/%{name}-%{version}.tar.gz
URL:		http://www.dockapps.org/file.php/id/315
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%if %{mdk}
Requires:	libdockapp0
BuildRequires:	libdockapp0-devel
%endif

%if %{fedora}
Requires:	libdockapp
BuildRequires:	libdockapp-devel
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

make DESTDIR=%{_bindir}                     \
	LIBDIR=-L%{_libdir}                 \
	INCDIR=-I%{_includedir}/X11

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 wmnethru $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{_bindir}/*

%changelog
* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> 0.1.1-4
- changed URL info to dockapps.org.

* Thu Aug 06 2009 J. Krebs <rpm_speedy@yahoo.com> 0.1.1-3
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> 0.1.1-2
- added distro info to release.

* Sat Sep 23 2006 J. Krebs <rpm_speedy@yahoo.com> 0.1.1-1
- initial build.
