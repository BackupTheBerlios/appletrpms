Summary: Clock Applet
Name: asclock
Version: 2.0.12
Release: 1
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
make BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/X11R6/bin/asclock
%doc


%changelog
* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 
- Initial build.


