%define prefix /usr/X11R6
%define name asmodem
%define version 0.6
%define release 3

Summary: Modem monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet monitors the modem.

%prep
tar -tvzf ../SOURCES/%{name}-%{version}-1.tar.gz
if [ -d  %{name}-%{version}-1 ] ; then 
    mv %{name}-%{version}-1 %{name}-%{version} 
    tar -cvzf ../SOURCES/%{name}-%{version}-1.tar.gz %{name}-%{version} 
fi
rm -rf %{name}-%{version}
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
* Sat Feb 26 2005 Sean Dague <sean@dague.net> 0.6-3
- really ugly work around for odd tarball version

* Sat Feb 26 2005 Sean Dague <sean@dague.net> 0.6-1-2
- change to asmodem versioning scheme

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1-1
- Initial build.



