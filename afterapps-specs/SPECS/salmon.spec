%define prefix /usr
%define name salmon
%define version 1.2.2
%define release 2

Summary: Still Another Load MONitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.mthoodcards.com/cgi-bin/index.py?grania
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A resource utilization monitor that can display the current
load averages, the amount of free or used memory and swap
space, memory in cache, buffers, and shared, number of
processes, the load split between user, nice, system, and
idle, the uptime, the current local time, the current
universal time, the name of the local host and the phase of
the moon.

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
%doc CHANGES INSTALL LICENSE README COPYING

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-1
- Initial build.
