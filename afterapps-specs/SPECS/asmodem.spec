%define prefix /usr/X11R6
%define name asmodem
%define version 0.6.1
%define release 1

Summary: Modem monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-0.6-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet monitors the modem.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 asmodem $RPM_BUILD_ROOT%prefix/bin
install -m 644 asmodem.man $RPM_BUILD_ROOT%prefix/man/man1/asmodem.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc INSTALL README


%changelog
* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1-1
- Initial build.



