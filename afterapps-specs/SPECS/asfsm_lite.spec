%define prefix /usr/X11R6
%define name asfsm_lite
%define version 1.0.0
%define release 1

Summary: File system monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet monitors the file system space.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 asfsm $RPM_BUILD_ROOT%prefix/bin
install -m 644 asfsm.man $RPM_BUILD_ROOT%prefix/man/man1/asfsm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc INSTALL README


%changelog
* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-1
- Initial build.



