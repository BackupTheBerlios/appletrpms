%define prefix /usr/X11R6
%define name wmweather+
%define version 2.9
%define release 3

%define generic 1
%define fedora 0
%{?_with_fedora:%define fedora 1}
%define mandrake 0
%{?_with_mandrake:%define mandrake 1}
%if %{fedora}
   %define generic 0
%endif
%if %{mandrake}
   %define generic 0
%endif

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

%if %{mandrake}
Requires: pcre
BuildRequires: pcre
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
* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.4-3
- Added if requires for pcre.

* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.4-2
- Added require for w3c-libwww.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 2.4-1
- Initial build.


