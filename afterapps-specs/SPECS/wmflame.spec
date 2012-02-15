%define		name wmflame
%define		version 0.6
%define		release 7%{?dist}

Summary:	wmflame is a WindowMaker dock applet that draws flames
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
Source:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-0.60.tar.gz
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
wmflame makes an animated flame. The flame algorithm is 
very standard. It is intended for a windowmaker/afterstep 
dock/wharf applet.

%prep
%setup -n %{name}.app

%build
cd %{name}

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS COPYING README
%{_bindir}/%{name}

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.6-7
- updated spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-6
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-5
- Updated Source path. Web site dead.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-4
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-3
- changed prefix path to /usr.

* Fri Jun 10 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-2
- replaced "copyright" with "license", updated .spec

* Tue Jul 27 1999 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release
