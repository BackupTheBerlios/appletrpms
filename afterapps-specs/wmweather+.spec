%define prefix /usr/X11R6
%define name wmweather+
%define version 2.4
%define release 1

Summary: A dock app for displaying weather information
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libpcre-devel libwraster-devel w3c-libwww-devel

%description
wmweather+ downloads current conditions, forecast data, and optionally a
radar image. It will also watch for various warnings and display them using an
external command.

%prep
%setup -q

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
* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 2.4-1
- Initial build.


