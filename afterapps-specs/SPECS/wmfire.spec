%define prefix /usr/X11R6
%define name wmfire
%define version 1.2.2
%define release 2

Summary: wmfire is a configurable cpu, mem, or network monitor.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.swanson.ukfsn.org/wmfire/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgtop2.0-devel

%description
This is an update of the original wmfire dock applet. It uses
the GDK library to improve its speed - using less than half the
cpu of the original program.

It can monitor the average cpu load, or individual cpu load on
SMP computers. Additionally it can monitor the memory, network
load, a file or just be set to show a pretty flame. On entering
the dock a burning spot replaces the cursor, and after two
seconds symbols to represent the current monitor are "burnt"
onscreen. The flame color can also be changed. 

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 src/wmfire $RPM_BUILD_ROOT%prefix/bin
install -m 644 wmfire.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README ALL_I_GET_IS_A_GREY_BOX


%changelog
* Sat Feb 26 2005 Sean Dague <sean@dague.net> 1.2.2-2
- add build requires for gtop2-devel

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-1
- Initial build.


