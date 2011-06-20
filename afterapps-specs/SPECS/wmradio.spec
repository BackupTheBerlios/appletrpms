%define		name wmradio
%define		version 0.9
%define		release 9%{?dist}

Summary:	FM radio card applet for WindowMaker
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tgz
Source1:	%{name}-setup-README
Patch0:		%{name}-%{version}-Makefile.in.patch
Patch1:		%{name}-%{version}-radio.c.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Buildrequires:	glibc-devel
Buildrequires:	libv4l-devel >= 0.8.3
Buildrequires:	libX11-devel
Buildrequires:	libXext-devel
Buildrequires:	libXpm-devel
Requires:	glibc
Requires:	libv4l
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	python < 3.0

%description
wmradio is FM radio card applet for WindowMaker 

%prep
%setup -q
%patch0
%patch1

%build
cp %{SOURCE1} .
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-libxosd --disable-gnome
make all

%install
rm -rf $RPM_BUILD_ROOT

make install wmradio DESTDIR=$RPM_BUILD_ROOT

make install-skins DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README wmradio-setup-README
%{_bindir}/wmradio
%{_bindir}/xwmradio
%{_bindir}/wmradio-remote
%{_bindir}/wmradio-config.py
%{_mandir}/man1/wmradio.*
%{_libdir}/wmradio/*.skin
%{_libdir}/wmradio/*.xpm
%{_datadir}/applications/%{name}-config.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue May 24 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.9-9
- shifted from kernel-headers to libv4l-devel for videodev.h.

* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.9-8
- cleaned up Makefile.in.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.9-7
- code cleanup.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9-6
- added libdir to configure for build under x86_64.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-5
- added distro info to release.

* Sun Mar 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9-4
- Updated Source path.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Mon May 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.
