%define		name salmon
%define		version 1.2.2
%define		release 6%{?dist}

Summary:	Sill Another Load MONitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://www.tigr.net/afterstep/view.php?applet=salmon/data
Source0:	http://tigr.net/afterstep/download/salmon/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libICE
Requires:	libjpeg-turbo
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libICE-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
A resource utilization monitor that can display the current
load averages, the amount of free or used memory and swap
space, memory in cache, buffers, and shared, number of
processes, the load split between user, nice, system, and
idle, the uptime, the current local time, the current
universal time, the name of the local host and the phase of
the moon.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README COPYING
%{_bindir}/salmon
%{_mandir}/man1/salmon.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-6
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-5
- added distro info to release.

* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-4
- updated wen page info.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-1
- Initial build.
