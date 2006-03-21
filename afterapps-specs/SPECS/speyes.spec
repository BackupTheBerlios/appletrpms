%define prefix /usr
%define name speyes
%define version 1.2.0
%define release 2

Summary: South Park-themed wmeyes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://okb-1.org/speyes/speyes.html
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.man
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
South Park-themed wmeyes.

%prep
%setup -q

%build
cp %{SOURCE1} .
xmkmf
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
install -s -m 755 speyes $RPM_BUILD_ROOT%prefix/bin/
install -m 644 speyes.man $RPM_BUILD_ROOT%prefix/man/man1/speyes.1
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc CHANGES README COPYING


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-2
- changed prefix path to /usr.

* Wed Mar 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.0-1
- Initial build.



