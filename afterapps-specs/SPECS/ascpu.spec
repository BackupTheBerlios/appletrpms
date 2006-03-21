%define prefix /usr
%define name ascpu
%define version 1.11
%define release 2

Summary: CPU monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
Packager: Sean Dague <sean@dague.net>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc CHANGES INSTALL LICENSE README TODO


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.11-2
- changed prefix path to /usr.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.11-1
- updated to 1.11

* Fri Aug 29 2003 Sean Dague <sean@dague.net> - 1.9-2
- added docs in

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 1.9-1
- Initial build.


