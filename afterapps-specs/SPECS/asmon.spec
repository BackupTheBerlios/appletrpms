%define prefix /usr
%define name asmon
%define version 0.65
%define release 2

Summary: AS system monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A system monitor applet for After Step.

%prep
%setup -q

%build
cd asmon
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
cd asmon
make PR_NAME=$RPM_BUILD_ROOT%prefix/bin/%name \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc AUTHOR CHANGES COPYING INSTALL 


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.65-2
- changed prefix path to /usr.

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - Aug 30, 2003
- Initial build.


