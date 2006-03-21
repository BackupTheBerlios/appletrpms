%define prefix /usr
%define name asmix
%define version 1.5
%define release 2

Summary: Sound volume knob
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet for changing the sound volume of your
music (well, not only music).  Looks and behaves like a
volume knob.

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
%doc CHANGES INSTALL LICENSE README


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.5-1
- Initial build.



