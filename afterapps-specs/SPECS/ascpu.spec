%define		name ascpu
%define		version 1.11
%define		release 6%{?dist}

Summary:	CPU monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=ascpu/data
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
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
This is an AfterStep look & feel CPU statistics monitor tool
for computers running Linux, FreeBSD, HP-UX or AIX.

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
%doc CHANGES LICENSE README TODO
%{_bindir}/ascpu
%{_mandir}/man1/ascpu.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.11-6
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.11-5
- added distro info to release.

* Fri Feb 23 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.11-4
- removed packager line.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.11-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.11-2
- changed prefix path to /usr.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.11-1
- updated to 1.11

* Fri Aug 29 2003 Sean Dague <sean@dague.net> - 1.9-2
- added docs in

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 1.9-1
- Initial build.


