%define version 0.70
%define release 2%{?dist}
%define name	xsensors

Summary:	displays motherboard sensor information via lm_sensors
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/System
URL:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.am.patch
Patch1:		%{name}-%{version}-configure.in.patch
Patch2:		%{name}-%{version}-gtk220.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	glib2
Requires:	glibc
Requires:	gtk2
Requires:	libpng
Requires:	lm_sensors >= 3.0.0
Requires:	pango
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gtk2-devel
BuildRequires:	libpng-devel
Buildrequires:	lm_sensors-devel >= 3.0.0
BuildRequires:	pango-devel

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
%{_bindir}/xsensors
%{_datadir}/pixmaps/xsensors/default.xpm

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.70-2
- linuxhardware.org is dead, shifted tarball to ftp.afterstep.org.

* Fri Jun 24 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.70-1
- initial build.
