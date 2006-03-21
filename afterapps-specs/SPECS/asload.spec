%define prefix /usr
%define name asload
%define version 0.9.4
%define release 2

Summary: CPU load monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet monitors the CPU load.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 asload $RPM_BUILD_ROOT%prefix/bin
install -m 644 asload.man $RPM_BUILD_ROOT%prefix/man/man1/asload.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc INSTALL LICENSE README


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-1
- Initial build.



