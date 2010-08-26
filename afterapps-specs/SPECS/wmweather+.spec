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

%define		name wmweather+
%define		version 2.12
%define		release 1%{?dist}

Summary:	A dock app for displaying weather information
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://sourceforge.net/project/showfiles.php?group_id=60336
Source0:	http://easynews.dl.sourceforge.net/sourceforge/wmweatherplus/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libcurl
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	w3c-libwww
Requires:	WindowMaker
BuildRequires:	glibc-devel
BuildRequires:	libcurl-devel
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	w3c-libwww-devel
BuildRequires:	WindowMaker-devel

%if %{mdk}
Requires:	libpcre0
BuildRequires:	libpcre0-devel
%endif

%if %{fedora}
Requires:	pcre
BuildRequires:	pcre-devel
%endif

%description
wmweather+ downloads current conditions, forecast data, and optionally a
radar image. It will also watch for various warnings and display them using an
external command.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make X_EXTRA_LIBS=" -lm"

%install

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc ChangeLog README HINTS example.conf


%changelog
* Wed Aug 25 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.12-1
- new version.

* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 2.11-2
- added compiler link to make for libm.

* Fri Apr 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 2.11-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.9-7
- added distro info to release.

* Wed Oct 25 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-6
- added build require for libwraster.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-4
- changed prefix path to /usr.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.9-3
- Added if requires for pcre.

* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.9-2
- Added require for w3c-libwww.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 2.9-1
- Initial build.


