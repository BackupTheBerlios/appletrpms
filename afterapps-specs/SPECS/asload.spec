%define		name asload
%define		version 0.9.4
%define		release 5%{?dist}

Summary:	system load monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=asload/data
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
A swallowable applet monitors the system load.

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
    install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/asload
%{_mandir}/man1/asload.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-5
- added spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-1
- Initial build.
