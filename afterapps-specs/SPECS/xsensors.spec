%define version 0.70
%define release 3%{?dist}
%define name	xsensors

Summary:	displays motherboard sensor information via lm_sensors
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/System
URL:		http://www.linuxhardware.org/xsensors/
Source0:	http://www.linuxhardware.org/xsensors/%{name}-%{version}.tar.gz
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

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=Xsensors
Comment=Displays motherboard sensor information via lm_sensors
Exec=xsensors
Icon=utilities-system-monitor
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category Monitor \
  --add-category System \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ABOUT-NLS AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_bindir}/xsensors
%{_datadir}/pixmaps/xsensors/default.xpm
%{_datadir}/applications/xsensors.desktop

%changelog
* Sat Jan 19 2013 J. Krebs <rpm_speedy@yahoo.com> - 0.70-3
- linuxhardware.org is alive, added desktop entry.

* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.70-2
- linuxhardware.org is dead, shifted tarball to ftp.afterstep.org.

* Fri Jun 24 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.70-1
- initial build.
