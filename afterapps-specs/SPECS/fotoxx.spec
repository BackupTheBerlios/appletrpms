%define name fotoxx
%define version 8.4
%define release 1%{?dist}

Summary: application for processing image files from a digital camera
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group: Applications/Multimedia
URL: http://kornelix.squarespace.com/%{name}/
Source0: http://kornelix.squarespace.com/storage/downloads/%{name}-%{version}.tar.gz
Patch0: %{name}-8.1-Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: gtk2 atk cairo pango libpng exiv2 libstdc++ ufraw perl-Image-ExifTool
Buildrequires: gtk2-devel atk-devel cairo-devel pango-devel libpng-devel libstdc++-devel gcc-c++ freeimage-devel ufraw perl-Image-ExifTool
Obsoletes: fotox
Provides: fotox

%description
Fotoxx is a free open-source Linux program for improving image files
made with a digital camera.

 The following functions are provided:

    * Show thumbnails of image files in a directory, navigate, choose
      files to view or edit.
    * Adjust overexposed or underexposed areas to improve visibility
      of detail (change brightness independently for different
      brightness levels).
    * Reduce fog or haze by removing "whiteness" and intensifying
      colors.
    * Edit whole image or an arbitrary area outlined with the mouse.
    * High dynamic range (HDR) photography: combine an underexposed
      and overexposed image to improve details visible in both bright
      and dark areas. Automatic image alignment.
    * Photo stitching or panorama: stitch two or more images together
      to make an ultra-wide image.
    * Simple image alignment and brightness / color matching.
    * Crop an image (choose the area of interest and cut-off the
      margins).
    * Rotate an image by any angle (level a tilted image, or turn in
      90 degree steps).
    * Resize an image, with convenience buttons for 2/3, 1/2, 1/3 and
      1/4 size.
    * Red-eye removal.

%prep
%setup -q
%patch0

%build
make PREFIX=%{_prefix} DOCDIR=%{_datadir}/doc/%{name}-%{version} DESKTOP=""

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} DOCDIR=%{_datadir}/doc/%{name}-%{version}

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=Fotoxx Digital Image Editor
Comment=Edit and improve digital camera image files
Exec=fotoxx
Icon=fotoxx.png
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                   \
  --add-category X-Red-Hat-Extra                                  \
  --add-category GTK                                              \
  --add-category 2DGraphics                                       \
  --add-category Graphics	                                  \
  %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 644 data/icons/fotoxx.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/icons/*
%{_datadir}/%{name}/locales/*
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*.gz

%changelog
* Mon Sep 13 2009 J. Krebs <rpm_speedy@yahoo.com> - 8.4-1
- new version.

* Mon Sep 08 2008 J. Krebs <rpm_speedy@yahoo.com> - 5.2.4-1
- new version.

* Sun Aug 24 2008 J. Krebs <rpm_speedy@yahoo.com> - 5.1-1
- new version.

* Sat Aug 16 2008 J. Krebs <rpm_speedy@yahoo.com> - 5.0.3-1
- new version.

* Sun Jul 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 4.9-1
- new version.

* Sat Jun 21 2008 J. Krebs <rpm_speedy@yahoo.com> - 4.7-1
- new version.

* Wed Jun 04 2008 J. Krebs <rpm_speedy@yahoo.com> - 4.5-2
- added fotox provide, to help yum users searching for fotox.

* Tue Jun 03 2008 J. Krebs <rpm_speedy@yahoo.com> - 4.5-1
- new version, application name changed from fotox to fotoxx.

* Sun May 25 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.44-1
- new version.

* Thu May 22 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.43-1
- new version.

* Mon Apr 21 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.41-1
- new version.

* Sat Apr 18 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.40-1
- new version.

* Sat Apr 12 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.39-1
- new version.

* Sun Mar 09 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.37-1
- Initial build.
