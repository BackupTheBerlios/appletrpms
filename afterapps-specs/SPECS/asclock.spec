%define prefix /usr/X11R6
%define name asclock
%define version 2.0.12
%define release 2

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
perl -pi -e 's{/usr/local/share/asclock/}{%prefix/share/%name}' config.c
make

%install
make BINDIR=$RPM_BUILD_ROOT%prefix/bin \
    MANDIR=$RPM_BUILD_ROOT%prefix/man/man1 \
    install install.man
install -d $RPM_BUILD_ROOT%prefix/share/%name
cp -a themes/* $RPM_BUILD_ROOT%prefix/share/%name


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%prefix/share/%name
%doc COPYING INSTALL README README.THEMES TODO


%changelog
* Sat Aug 30 2003 Sean Dague <sean@dague.net> - 2.0.12-2
- Add in theme support

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 
- Initial build.


