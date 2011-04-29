%define	name 	libAfterImage-NoX
%define	version	1.20
%define	release	1%{?dist}
%define	epoch	20

Summary:	A generic image manipulation library (Non-Xfree/Xorg version)
Name:		%name
Version:	%version
Release:	%release
Epoch:		%epoch
License:	GPLv2+
Group:		System Environment/Libraries
Source0:	ftp://ftp.afterstep.org/stable/libAfterImage/libAfterImage-%{version}.tar.gz
Source1:	%{name}-COPYING
Source2:	%{name}-COPYING.LDP
Source3:	%{name}-COPYING.LIB
URL:		http://www.afterstep.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	librsvg2
Requires:	libtiff
Requires:	libjpeg
Requires:	libpng
Requires:	freetype
Requires:	zlib
BuildRequires:	librsvg2-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:  freetype-devel
BuildRequires:  zlib-devel
Conflicts:	libX11 AfterStep aterm urxvt libAfterImage xorg-x11-filesystem
Provides:	libAfterImage

%description
Non-Xfree/Xorg version of libAfterImage, useful for server applications.

libAfterImage is a generic image manipulation library. It was initially
implemented to address AfterStep Window Manager\'s needs for image handling,
but it evolved into extremely powerful and flexible software, suitable for
virtually any project that has needs for loading, manipulating, displaying
images, as well as writing images in files. Most of the popular image formats
are supported using standard libraries, with XCF, XPM, PPM/PNM, BMP, ICO,
TGA and GIF being supported internally.

PNG, JPEG and TIFF formats are supported via standard libraries.

Powerful text rendering capabilities included, providing support for
TrueType fonts using FreeType library, and antialiasing of standard fonts
from X window system.

%package devel
Summary:	Files needed for software development with libAfterImage (Non-Xfree/Xorg version)
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	GPL
Group:		Development/Libraries
Requires:	librsvg2-devel
Requires:	libtiff-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	freetype-devel
Requires:	zlib-devel
Conflicts:	libX11 libX11-devel xorg-x11-filesystem AfterStep-devel libAfterImage-devel
Requires:	libAfterImage-NoX = %{epoch}:%{version}
Provides:	libAfterImage-devel

%description devel
Non-Xfree/Xorg version of libAfterImage-devel, useful for server applications.

The libAfterImage-devel package contains the files needed for development with
libAfterImage.

%prep
%setup -q -n libAfterImage-%{version}

%build

./configure --prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--without-x \
	--enable-i18n \
	--enable-sharedlibs

make LIBS_X=" -lXext -lX11"

%install

cp %{SOURCE1} COPYING
cp %{SOURCE2} COPYING.LDP
cp %{SOURCE3} COPYING.LIB

rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install

rm -rf $RPM_BUILD_ROOT/%{_datadir}/libAfterImage/doc/html/*
rm -rf $RPM_BUILD_ROOT/%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING COPYING.LDP COPYING.LIB doc/html/
%{_bindir}/afterimage*
%{_bindir}/ascompose
%{_bindir}/asflip
%{_bindir}/asgrad
%{_bindir}/asi18n
%{_bindir}/asmerge
%{_bindir}/asscale
%{_bindir}/astext
%{_bindir}/astile
%{_bindir}/asvector
%{_bindir}/asview
%{_libdir}/libAfterImage.so.0*
%{_mandir}/man3/*

%files devel
%defattr(-,root,root)
%{_libdir}/libAfterImage.so
%dir %{_includedir}/libAfterImage
%{_includedir}/libAfterImage/*

%changelog
* Sat Jan 15 2011 J. Krebs <rpm_speedy@yahoo.com> 1.20-1
- new version.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> 1.18-1
- new version.

* Sat Oct 20 2007 J. Krebs <rpm_speedy@yahoo.com> 1.15-2
- fixed typo in requires for -devel (libaiver wasn't defined).

* Mon Aug 19 2007 J. Krebs <rpm_speedy@yahoo.com> 1.15-1
- initial build.
