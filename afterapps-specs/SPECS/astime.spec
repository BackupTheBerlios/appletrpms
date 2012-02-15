%define		name astime
%define		version 2.8
%define		release 6%{?dist}

Summary:	An analog clock
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=astime/data
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
An analog clock that shows the time, the date and the day of
week.  Highly customizable to satisfy the needs of almost any
user.

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
%doc CHANGES LICENSE README *.astimerc
%{_bindir}/astime
%{_mandir}/man1/astime.*


%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.8-6
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.8-5
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.8-4
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.8-3
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.8-2
- Added example .astimerc to the docs area.

* Thu Feb 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.8-1
- Initial build.



