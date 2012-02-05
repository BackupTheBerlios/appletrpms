%define		name asmon
%define		version 0.65
%define		release 5%{?dist}

Summary:	AS system monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=asmon/data
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
A system monitor applet for AfterStep.

%prep
%setup -q

%build
cd asmon
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd asmon
make PR_NAME=$RPM_BUILD_ROOT%{_bindir}/%name \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHOR CHANGES COPYING
%{_bindir}/asmon

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.65-5
- updated requires to .spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.65-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.65-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.65-2
- changed prefix path to /usr.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - Aug 30, 2003
- Initial build.
