%define prefix /usr/X11R6
%define name wmweather+
%define version 2.4
%define release 1

Summary: WM Weather Applet
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libpcre-devel libwraster-devel

%description
This is an AfterStep look & feel CPU statistics monitor tool
for computers running Linux, FreeBSD, HP-UX or AIX.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%prefix/bin \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%prefix/man/man1 \
    install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc CHANGES INSTALL LICENSE README TODO example.conf


%changelog
* Fri Aug 22 2003 Sean Dague <sean@dague.net> - Aug 30, 2003
- Initial build.


