%define version 0.70
%define release 1%{?dist}
%define name	xsensors

Summary:	displays motherboard sensor information via lm_sensors
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/System
Source0:	http://www.linuxhardware.org/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.am.patch
Patch1:		%{name}-%{version}-configure.in.patch
Patch2:		%{name}-%{version}-gtk220.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	lm_sensors >= 3.0.0 gtk2
Buildrequires:	lm_sensors-devel >= 3.0.0 gtk2-devel

%description
This is another release of xsensors, a program designed to display all
the related information from your motherboard sensors.  This information is
gathered via lm_sensors, the software drivers that actually gathers the 
sensor information.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
./autogen.sh

./configure --prefix=%{_prefix}

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ABOUT-NLS AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/pixmaps/xsensors/*

%changelog
* Fri Jun 24 2011 J. Krebs <rpm_speedy@yahoo.com> 0.70-1
- initial build.
