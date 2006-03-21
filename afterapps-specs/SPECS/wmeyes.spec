%define prefix /usr
%define name wmeyes
%define version 1.2
%define release 2

Summary: wmeyes is a dockapp with moving eyes that follow mouse movement
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.bstern.org/wmeyes/
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.man
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmeyes is a dockapp with moving eyes that follow mouse movement.
This version also allows execition of a command by clicking the icon.

%prep
%setup -q

%build
cp %{SOURCE1} .
xmkmf
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
install -s -m 755 wmeyes $RPM_BUILD_ROOT%prefix/bin/
install -m 644 wmeyes.man $RPM_BUILD_ROOT%prefix/man/man1/wmeyes.1
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc ChangeLog README LICENSE


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2-2
- changed prefix path to /usr.

* Thu Mar 24 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2-1
- Initial build.



