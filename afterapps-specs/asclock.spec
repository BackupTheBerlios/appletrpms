%define prefix /usr/X11R6
%define name asclock
%define version 2.0.12
%define release 1

Summary: Clock Applet
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AfterStep clock applet

%prep
%setup -q

%build
echo -e "shaped\n\n" | ./configure
make

%install
make BINDIR=$RPM_BUILD_ROOT%prefix/bin \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/X11R6/bin/*
%doc


%changelog
* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 
- Initial build.


