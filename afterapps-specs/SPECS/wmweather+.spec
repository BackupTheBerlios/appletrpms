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

%define prefix /usr
%define name wmweather+
%define version 2.9
%define release 4

Summary: A dock app for displaying weather information
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
Patch0: wmweather+-fedorafix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: w3c-libwww-devel
Requires: w3c-libwww

%if %{mdk}
Requires: libpcre0
BuildRequires: libpcre0-devel
%endif

%if %{fedora}
Requires: pcre
BuildRequires: pcre-devel
%endif

%description
wmweather+ downloads current conditions, forecast data, and optionally a
radar image. It will also watch for various warnings and display them using an
external command.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
make prefix=$RPM_BUILD_ROOT%prefix \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc ChangeLog README HINTS example.conf


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.9-4
- changed prefix path to /usr.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.9-3
- Added if requires for pcre.

* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.9-2
- Added require for w3c-libwww.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 2.9-1
- Initial build.


