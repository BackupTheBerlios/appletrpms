%define		name wmcpuload
%define		version 1.1.0pre5
%define		release 6%{?dist}

Summary:	CPU monitor dockapp which has an LCD look user interface
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.dockapps.org/file.php/id/36
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
WMCPULoad is a CPU monitor dockapp which has an LCD look-alike
user interface, and displays the current usage, expressed as a
percentile and a chart, The back-light may be turned on/off by
clicking the mouse button over the application. If the CPU usage
hits a certain threshold, an alarm-mode will alert you by turning
back-light on. 

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 src/wmcpuload $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO


%changelog
* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre5-6
- changed URL info to dockapps.org.

* Sun Sep 13 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre5-5
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre5-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre5-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre5-2
- changed prefix path to /usr.

* Sat Mar 11 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre5-1
- Initial build.

* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre4-1
- Initial build.
