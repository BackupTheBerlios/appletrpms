Summary: APM monitor
Name: asapm
Version: 2.13
Release: 1
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AfterStep APM monitor

%prep
%setup -q

%build
./configure --prefix=/usr/X11R6
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/X11R6/bin/asapm
/usr/X11R6/man/man1/asapm.1x*
%doc


%changelog
* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 
- Initial build.


