%define prefix /usr/X11R6
%define name wminet
%define version 3.0.0
%define release 1

Summary: dockapp for monitoring internet connections to/from your computer
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.swanson.ukfsn.org/#wminet
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Very useful dock app for monitoring internet connections to and
from your computer. The number of connections can be filtered
based on local and remote addresses and ports, on either tcp or
udp. It can also display hostname and number of processes.

Includes both standard and LCD-style displays.

This new version uses a lot less CPU and allows greater
configuration. The ability to monitor httpd and ftpd processes,
nfs mounts and lpd queues has been removed from the original. 

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 src/wminet $RPM_BUILD_ROOT%prefix/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README wminetrc


%changelog
* Fri Mar 25 2005 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-1
- Initial build.



