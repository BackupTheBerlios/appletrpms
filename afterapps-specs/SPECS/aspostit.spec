%define		name aspostit
%define		version 1.3
%define		release 6%{?dist}

Summary:	Post-It notes applet/dockapp
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=aspostit/data
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-xpostit.c-include.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libICE
Requires:	libjpeg-turbo
Requires:	libSM
Requires:	libX11
Requires:	libXaw
Requires:	libXext
Requires:	libXpm
Requires:	libXmu
Requires:	libXt
BuildRequires:	glibc-devel
BuildRequires:	libICE-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXaw-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXmu-devel
BuildRequires:	libXt-devel

%description
A swallowable applet allows you to ceate notes in post-it like
style.  The notesare saved in your home directory and are
automatically loaded on the next startup.

%prep
%setup -q
%patch0

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
%doc BUGS CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.3-6
- updated spec file.

* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3-5
- added requires for libXaw.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.3-1
- Initial build.



