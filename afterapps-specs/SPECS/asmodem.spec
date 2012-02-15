%define		name asmodem
%define		version 0.6
%define		release 7%{?dist}

Summary:	Modem monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=asmodem/data
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}-1.tar.gz
Patch0:		%{name}-%{version}-copying.patch
Patch1:		%{name}-%{version}-license.patch
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
A swallowable applet monitors the modem.

%prep
%setup -q -n %{name}-%{version}-1
%patch0
%patch1

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
%doc COPYING LICENSE README
%{_bindir}/asmodem
%{_mandir}/man1/asmodem.*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.6-7
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-6
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-4
- changed prefix path to /usr.

* Sat Feb 26 2005 Sean Dague <sean@dague.net> - 0.6-3
- really ugly work around for odd tarball version

* Sat Feb 26 2005 Sean Dague <sean@dague.net> - 0.6-1-2
- change to asmodem versioning scheme

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1-1
- Initial build.



