### BEGIN Distro Defines
%define mdk  %(if [ -e /etc/mandrake-release -o -e /etc/mandriva-release ]; then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

#%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
#%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1

%if %{mdk}
  %define generic 0
%endif

%if %{fedora}
  %define generic 0
  %define fcver $(grep release /etc/fedora-release | cut -d ' ' -f4)
  %define fver $(grep release /etc/fedora-release | cut -d ' ' -f2)
  %define fedora7 %(if [ %fver = release ]; then echo 1; else echo 0; fi;)
  %{?_with_fedora7:   %{expand: %%global fedora7 1}}
  %define fedora5 %(if [ %fcver -ge 5 ]; then echo 1; else echo 0; fi;)
  %{?_with_fedora5:   %{expand: %%global fedora5 1}}
  %define fedora4 %(if [ %fcver -le 4 ]; then echo 1; else echo 0; fi;)
  %{?_with_fedora4:   %{expand: %%global fedora4 1}}  
  %if %{fedora7}
    %define fedora5 1
    %define fedora4 0
  %endif
%endif

#%if %{suse}
#  %define generic 0
#%endif

%define ismultiarch 0
%{?multiarch:%define ismultiarch 1}
### END Distro Definitions

%define	name AfterStep
%define	version	2.2.9
%define	libaiver	1.19
%define	libabver	1.13
%define	libairel	3%{?dist}
%define	libabrel	3%{?dist}
%define release 3%{?dist}
%define epoch 20

Summary:	AfterStep Window Manager (NeXTalike)
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.afterstep.org
Vendor:		The AfterStep Team (see TEAM in docdir)
Source0:	ftp://ftp.afterstep.org/stable/%{name}-%{version}.tar.gz
Source1:	Xclients.afterstep.switchdesk
Source2:	afterstep.gdm
Source3: 	AfterStep.kdm
Source4: 	AfterStep.menu
Source5: 	AfterStep.menumethod
Source6: 	afterstep.desktop.xsessions
Source7: 	afterstep.desktop.wm-properties
Source8:	afterstep.fedora.README
Source9:	%{name}-2.2.7-wharf.alternate
Patch0:		%{name}-2.2.5-ImageMagick.patch
Patch1:		%{name}-2.2.7-winlist.patch
Patch2:		%{name}-2.2.7-pager.patch
Patch3:		%{name}-2.2.9-asgtklookedit.c.patch
Patch4:		%{name}-2.2.9-ascompose.c.patch
Patch5:		%{name}-2.2.9-screen.c.patch
Patch6:		%{name}-2.2.9-asdatabase.h.patch
Patch7:		%{name}-2.2.9-Database.c.patch
Patch8:		%{name}-2.2.9-hints.c.patch
Patch9:		%{name}-2.2.9-hints.h.patch
Patch10:	%{name}-2.2.9-afterbase.c.patch
Patch11:	%{name}-2.2.9-afterconf.h.patch
Patch12:	%{name}-2.2.9-afterstep.c.patch
Patch13:	%{name}-2.2.9-AfterStep.c.patch
Patch14:	%{name}-2.2.9-asapp.c.patch
Patch15:	%{name}-2.2.9-ascolor.c.patch
Patch16:	%{name}-2.2.9-ASDocGen.c.patch
Patch17:	%{name}-2.2.9-asfeel.h.patch
Patch18:	%{name}-2.2.9-asim_afterbase.h.patch
Patch19:	%{name}-2.2.9-asimbrowser.c.patch
Patch20:	%{name}-2.2.9-configure.c.patch
Patch21:	%{name}-2.2.9-Feel.c.patch
Patch22:	%{name}-2.2.9-NEW.patch
Patch23:	%{name}-2.2.9-pager.c.patch
Patch24:	%{name}-2.2.9-Pager.c.patch
Patch25:	%{name}-2.2.9-WinList.c.patch
Patch26:	%{name}-2.2.9-WinTabs.c.patch
Distribution:	The AfterStep TEAM
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if %{mdk}
Obsoletes:	libAfterStep1
%endif
Provides:	AfterStep-libs
Requires: 	libAfterImage = %{epoch}:%{libaiver}-%libairel
Requires:	readline
Requires:	gtk2, gtk2-devel
Requires:	feh
Requires:	libXt
BuildRequires:  readline-devel
BuildRequires:  gtk2-devel
BuildRequires:	librsvg2-devel
BuildRequires:	libtiff-devel
BuildRequires:  freetype-devel
BuildRequires:  zlib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel

%description
AfterStep is a Window Manager for X which started by emulating the
NEXTSTEP look and feel, but which has been significantly altered
according to the requests of various users. Many adepts will tell you
that NEXTSTEP is not only the most visually pleasant interface, but
also one of the most functional and intuitive out there. AfterStep
aims to incorporate the advantages of the NEXTSTEP interface, and add
additional useful features.

The developers of AfterStep have also worked very hard to ensure
stability and a small program footprint. Without giving up too many
features, AfterStep still works nicely in environments where memory is
at a premium.

%package devel
Summary:	Files needed for software development with AfterStep
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	GPL
Group:		Development/Libraries
Requires: 	libAfterImage-devel = %{epoch}:%{libaiver}-%libairel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files needed for software development with AfterStep.

%package -n libAfterImage
Summary:	A generic image manipulation library
Version:	%{libaiver}
Release:	%libairel
Epoch:		%{epoch}
License:	GPL
Group:		System Environment/Libraries
Provides:	libAfterImage
Requires:	librsvg2
Requires:	libtiff
Requires:	libpng
Requires:	libjpeg
Requires:	freetype
Requires:	zlib
Requires:	libX11
Requires:	libAfterBase = %{epoch}:%{libabver}-%libabrel

%description -n libAfterImage
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

%package -n libAfterImage-devel
Summary:	Files needed for software development with libAfterImage
Version:	%{libaiver}
Release:	%libairel
Epoch:		%{epoch}
License:	GPL
Group:		Development/Libraries
Requires:	librsvg2-devel
Requires:	libtiff-devel
Requires:	libpng-devel
Requires:	libjpeg-devel
Requires:	freetype-devel
Requires:	zlib-devel
Requires:	libX11-devel
Requires:	libAfterImage = %{epoch}:%{libaiver}-%libairel
Requires:	libAfterBase-devel = %{epoch}:%{libabver}-%libabrel

%description -n libAfterImage-devel
The libAfterImage-devel package contains the files needed for development with
libAfterImage

%package -n libAfterBase
Summary:	A basic functions library providing support for libAfterImage
Version:	%{libabver}
Release:	%libabrel
Epoch:		%{epoch}
License:	GPL
Group:		System Environment/Libraries

%description -n libAfterBase
A basic functions library providing support for libAfterImage.

%package -n libAfterBase-devel
Summary:	Files needed for software development with libAfterBase
Version:	%{libabver}
Release:	%libabrel
Epoch:		%{epoch}
License:	GPL
Group:		Development/Libraries
Requires:	libAfterBase = %{epoch}:%{libabver}-%libabrel

%description -n libAfterBase-devel
Files needed for software development with libAfterBase.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch12
%patch13
%patch14
%patch15
%patch16
%patch17
%patch18
%patch19
%patch20
%patch21
%patch22
%patch23
%patch24
%patch25
%patch26

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure \
	--prefix=%{_prefix}                       \
	--libdir=%{_libdir}                       \
	--mandir=%{_mandir}                       \
	--enable-sharedlibs                       \
	--disable-staticlibs                      \
	--enable-i18n                             \
	--with-helpcommand="xterm -e man"         \
	--with-desktops=2 --with-deskgeometry=2x2 \
	--with-imageloader="feh --bg-center"

make

if [[ -x /usr/bin/sgml2html ]]; then sgml2html doc/afterstep.sgml; fi
cd src/ASDocGen && ./ASDocGen -l log.html -t html && cd ../..

#for cvs builds - should be OK on release.
rm -rf afterstep/start/0_Applications/Office/Open_Office/
rm -rf afterstep/start/1_Desktop/Animations/
rm -rf afterstep/start/1_Desktop/Pictures/GNOME_Branded/
rm -rf afterstep/start/1_Desktop/Pictures/GNOME_Nature/
rm -rf afterstep/start/1_Desktop/Pictures/GNOME_Tiles/
rm -rf afterstep/start/1_Desktop/Pictures/GNOME_Translucent/
rm -rf afterstep/start/2_Modules/Forms/
rm -rf afterstep/start/2_Modules/Scripts/
rm -rf afterstep/start/2_Modules/Stop/

mv afterstep/wharf afterstep/wharf.orig
cp %{SOURCE9} afterstep/wharf

%install
if [[ -d $RPM_BUILD_ROOT ]]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install
rm -f $RPM_BUILD_ROOT%{_bindir}/{sessreg,xpmroot}

#fedora core 4 and earlier gdm setup
%if %{fedora4}
cp %{SOURCE8} .
install -d $RPM_BUILD_ROOT%{_datadir}/switchdesk/
install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/switchdesk/Xclients.afterstep
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/gdm/Sessions/
install -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/gdm/Sessions/afterstep
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions/
install -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/afterstep.desktop
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/
install -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/afterstep.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/AfterStep.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/xsessions/AfterStep.desktop
%endif

#fedora core 5 and later gdm setup
%if %{fedora5}
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions/
install -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/afterstep.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/AfterStep.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/xsessions/AfterStep.desktop
%endif

# mandrake/mandriva menu items
%if %{mdk}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/42AfterStep
install -d $RPM_BUILD_ROOT%{_libdir}/menu/afterstep
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/menu/afterstep
install -d $RPM_BUILD_ROOT%{_sysconfdir}/menu-methods/
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/menu-methods/AfterStep
%endif

%if %{ismultiarch}
#mkdir -p $RPM_BUILD_ROOT%{multiarch_bindir}
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/afterimage-config
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/afterimage-libs
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/afterstep-config
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/asgtk-config
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEW README* TEAM UPGRADE doc/languages doc/licences doc/code TODO doc/*.html doc/licences/COPYING*
%doc src/ASDocGen/html/*html
%{_bindir}/ASFileBrowser
%{_bindir}/ASRun
%{_bindir}/ASWallpaper
%{_bindir}/Animate
%{_bindir}/Arrange
%{_bindir}/Banner
%{_bindir}/GWCommand
%{_bindir}/Ident
%{_bindir}/MonitorWharf
%{_bindir}/Pager
%{_bindir}/PrintDesktopEntries
%{_bindir}/Wharf
%{_bindir}/WinCommand
%{_bindir}/WinList
%{_bindir}/WinTabs
%{_bindir}/Xpm2Jpg
%{_bindir}/afterstep
%{_bindir}/afterstep-config
%{_bindir}/afterstepdoc
%{_bindir}/ascolor
%{_bindir}/ascommand.pl
%{_bindir}/asgtk-config
%{_bindir}/ascheckttf
%{_bindir}/importasmenu
%{_bindir}/installastheme.pl
%{_bindir}/makeastheme.pl
%{_bindir}/postcard.sh
%dir %{_datadir}/afterstep
%{_datadir}/afterstep/*
%{_libdir}/libASGTK.so.1*
%{_libdir}/libAfterConf.so.1*
%{_libdir}/libAfterStep.so.1*
%{_mandir}/man1/*
# this is evil hack, but I can't get it to work otherwise on mdk
%if !%{fedora}
%config %{_sysconfdir}/X11/wmsession.d/42AfterStep
%{_sysconfdir}/menu-methods/AfterStep
%{_datadir}/xsessions/AfterStep.desktop
%config %{_libdir}/menu/afterstep/AfterStep.menu
%endif
%if %{fedora5}
%{_datadir}/xsessions/afterstep.desktop
%endif
%if %{fedora4}
%{_sysconfdir}/X11/gdm/Sessions/afterstep
%{_datadir}/switchdesk/Xclients.afterstep
%{_datadir}/xsessions/afterstep.desktop
%{_datadir}/gnome/wm-properties/afterstep.desktop
%doc afterstep.fedora.README
%endif
%if %{generic}
%{_prefix}/xsessions/AfterStep.desktop
%endif

%files devel
%defattr(-,root,root)
%dir %{_includedir}/libAfterConf
%dir %{_includedir}/libAfterStep
%dir %{_includedir}/libASGTK
%{_libdir}/libASGTK.so
%{_libdir}/libAfterConf.so
%{_libdir}/libAfterStep.so
%{_includedir}/libAfterConf/*
%{_includedir}/libAfterStep/*
%{_includedir}/libASGTK/*
%{_mandir}/man3/*
%doc src/ASDocGen/html/API/*html

%files -n libAfterImage
%defattr(-,root,root)
%doc libAfterImage/ChangeLog libAfterImage/README doc/licences/COPYING*
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

%files -n libAfterImage-devel
%defattr(-,root,root)
%{_libdir}/libAfterImage.so
%dir %{_includedir}/libAfterImage
%{_includedir}/libAfterImage/*

%files -n libAfterBase
%defattr(-,root,root)
%doc doc/licences/COPYING*
%{_libdir}/libAfterBase.so.0*

%files -n libAfterBase-devel
%defattr(-,root,root)
%{_libdir}/libAfterBase.so
%dir %{_includedir}/libAfterBase
%{_includedir}/libAfterBase/*

%pre
for i in /usr /usr/local /usr/X11R6 ; do
	if [ -d $i/share/afterstep_old ]; then
		rm -r $i/share/afterstep_old;
	fi
	# %config /usr/share/afterstep should take care of this.
	#if [ -d $i/share/afterstep ]; then
	#	cp -pr $i/share/afterstep $i/share/afterstep_old;
	#	exit;
	#fi
done

%post
/sbin/ldconfig

if [ -x /usr/sbin/fndSession ]; then /usr/sbin/fndSession || true ; fi

%postun
/sbin/ldconfig

if [ -x /usr/sbin/fndSession ]; then /usr/sbin/fndSession || true ; fi

%changelog
* Sun Nov 01 2009 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.9-3
- added more fixes and patches for -v, brought in-line with cvs.

* Thu Oct 29 2009 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.9-2
- added patches for glibc segfaults.

* Thu Jul 30 2009 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.9-1
- new version.

* Sat May 31 2008 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.8-3
- Changed image loader from qiv to feh.

* Mon Mar 24 2008 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.8-2
- Pager fix added to fix issues when swallowed by Wharf.

* Wed Mar 17 2008 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.8-1
- new version.

* Thu Dec 06 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.7-4
- added patch to skip short duration windows under workspace_state.

* Thu Dec 06 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.7-3
- added patches to look for urxvt (then aterm, rxvt, xterm).

* Fri Nov 09 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.7-2
- cleaned-up desktop.

* Mon Aug 27 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.7-1
- new version.

* Thu Aug 02 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.6-3
- broke-out libAI and libAB as separate packages for those
  wanting to run rxvt-unicode and aterm without AfterStep.
  Rxvt-unicode will need libAI >= 1.15, and a separate
  package makes it easier to differentiate.
- added qiv as a require for AfterStep - some apps still need
  an image loader other than that provided by AfterStep.

* Thu Jun 14 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.6-2
- added test for F7.

* Thu Jun 14 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.6-2
- added test for F7.

* Wed May 30 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.6-1
- new version.

* Fri May 04 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.5-3
- added rpm macro libdir to configure.

* Wed May 02 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.5-2
- added MMX patches for x86_64.

* Fri Apr 27 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.5-1
- new version.

* Mon Feb 19 2007 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.4-2
- removed debug entries from /usr/lib, added provides for libAI.

* Mon Nov 20 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.4-1
- new version.

* Tue Oct 11 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.3-1
- new version.

* Wed May 25 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.2-1
- new version.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.1-3
- changed prefix path to /usr.

* Thu Mar  9 2006 Sean Dague <sean@dague.net> - 20:2.2.1-1
- bring up to 2.2.1 release
- make find session call on Mandrake, so it actually shows up in kdm

* Mon Jan 09 2006 J. Krebs <rpm_speedy@yahoo.com> 20:2.2.0-1
- brought up to 2.1.2 release.
- updated distro defines.

* Mon Aug 08 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.2-2
- updated configuration defines.

* Sat Jul 23 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.2-1
- brought up to 2.1.2 release.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-6
- removed xloadimage with qiv. FC4 no longer provides xloadimage.
- qiv is an optional package and not a require for install.

* Sun Jun 12 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-5
- added epoch info back in and tweaked requires.

* Fri Jun 10 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-4
- AfterStep now works correctly under Fedora gdm & switchdesk.

* Fri Jun 10 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-3
- replaced "copyright" with "license" .spec file.

* Thu Jun 09 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-2
- eliminated epoch and fver from .spec file.

* Mon Jun 06 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-1
- brought up to 2.1.1 release.

* Tue May 17 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.0-1
- brought up to 2.1.0 release.

* Wed May 04 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.00.05-1
- brought up to 2.00.05 release.

* Mon Mar 28 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.00.04-2
- Activated postcard-to-developer.

* Tue Mar 22 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.00.04-1
- brought up to 2.00.04 release

* Mon Mar  7 2005 Sean Dague <sean@dague.net> 20:2.00.03-3
- set provides manually on libs, move some docs to main and devel

* Sun Mar  6 2005 Sean Dague <sean@dague.net> 20:2.00.03-2
- add with tagging to fedora vs. mandrake issues

* Thu Mar 03 2005 J.Krebs <rpm_speedy@yahoo.com> 20:2.00.03-1
- brought up to 2.00.03 release
- separated Fedora desktop config files into a separate rpm

* Sat Feb 26 2005 Sean Dague <sean@dague.net> 20:2.00.02-2
- brought up to 2.00.02 release

* Wed Sep 28 2004 Graydon Saunders <graydon@epiphyte.net> 2.00.00
- added %%{prefix}
- added the man pages to the -libs package

* Sun Dec 14 2003 Andre Costa <acosta@ar.microlink.com.br>
- split into three different RPMs
- AfterStep-libs is now required for AfterStep
- use qiv instead of xv for root image
- removed check for buildroot location on %clean
- removed references to RH startmenu

* Mon Dec 6 1999 David Mihm <webmaster@afterstep.org>
  [AfterStep-1.7.149-1]
- Updated to current version

* Wed Jun 9 1999 David Mihm <webmaster@afterstep.org>
  [AfterStep-1.7.111-1]
- Now this spec file is included in the distribution.
- Upgrade to latest snaphost 1.7.111
- Many thanks to Ryan Weaver for this spec file to include!!

* Tue Jun  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.7.108-2]
- Made changes to spec to configure and install more like RedHat
  installations.
- Added %config to the /usr/share/afterstep listing to allow rpm to
  backup this dir if needed.

* Tue Jun  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.7.108-1]
- Added patches 16-18 to make version 1.7.108

* Fri May 28 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.7.105-1]
- Upgraded to 1.7.90 and added patches 1-15 to make it version 1.7.105.
- Made RPM relocatable.
- Building dynamic libs instead of static.

* Mon Feb  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.6.10-1]
- Upgraded to 1.6.10

* Mon Jan  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.6.6-3]
- Added a pre-install script to check to see if a previous versions
  share directory exists... If one does, it will copy it to afterstep_old.

* Thu Dec 31 1998 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.6.6-2]
- Configuring with no special settings and installing into
  default dirs as per David Mihm <davemann@ionet.net>
