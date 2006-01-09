### BEGIN Distro Defines
### mdk, fedora, suse & generic are distros
### mandriva, fedoragcc4, and susegcc4 define gcc 4.0 compilers
%define mdk  %(if [ -e /etc/mandrake-release -o -e /etc/mandriva-release ];\
 then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define mandriva  %(if [ -e /etc/mandriva-release ]; then echo 1; else echo 0; fi;)
%{?_with_mandriva:   %{expand: %%global mandriva 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1

%if %{mdk}
  %define generic 0
%endif

%if %{fedora}
  %define generic 0
  %define fcgcctest $(grep release /etc/fedora-release | cut -d ' ' -f4)
  %define fedoragcc4 %(if [ %fcgcctest -ge 4 ]; then echo 1; else echo 0; fi;)
  %{?_with_fedoragcc4:   %{expand: %%global fedoragcc4 1}}
%endif

%if %{suse}
  %define generic 0
  %define susegcctest $(grep VERSION /etc/SuSE-release | cut -d ' ' -f3)
  %define susegcc4 %(if [ %susegcctest -ge 10.0 ]; then echo 1; else echo 0; fi;)
  %{?_with_susegcc4:   %{expand: %%global susegcc4 1}}
%endif

%define ismultiarch 0
%{?multiarch:%define ismultiarch 1}
### END Distro Definitions

%define	name AfterStep
%define	version	2.2.0
%define release 1

%define epoch 20
%define gdesk /usr/share

%define __prefix /usr/X11R6
%define _mandir %{__prefix}/man
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _includedir %{__prefix}/include
%define _libdir %{__prefix}/lib

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
Distribution:	The AfterStep TEAM
Packager:	Sean Dague <sean at dague dot net>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	%{name}-libs = %{epoch}:%{version}

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

%package libs
summary:	libraries required by afterstep 2.0
version:	%{version}
release:	%{release}
Epoch:		%{epoch}
License:	GPL
group:		User Interface/Desktops
Provides: 	%{name}-libs
%if %{mdk}
Obsoletes: libAfterStep1
%endif

%description libs
  Libraries neeeded by AfterStep 2.0

%package devel
summary:	AfterStep libs include files
version:	%{version}
release:	%{release}
Epoch:		%{epoch}
License:	GPL
group:		User Interface/Desktops
Requires: 	%{name}-libs = %{epoch}:%{version}

%description devel
  AfterStep libs include files

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure \
	--prefix=%{__prefix}                      \
	--enable-sharedlibs                       \
	--disable-staticlibs			  \
	--enable-ascp                             \
	--enable-i18n                             \
	--with-helpcommand="aterm -e man"         \
	--with-desktops=1 --with-deskgeometry=2x3 \
	--with-imageloader="qiv --root"

make

if [[ -x /usr/bin/sgml2html ]]; then sgml2html doc/afterstep.sgml; fi
cd src/ASDocGen && ./ASDocGen -l log.html -t html && cd ../..

%install
if [[ -d $RPM_BUILD_ROOT ]]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install
rm -f $RPM_BUILD_ROOT%{_bindir}/{sessreg,xpmroot}
#for f in libAfter{Base,Conf,Image,Step}; do
#   cp -a $f/$f.so* %{buildroot}%{_libdir}
#done

%if %{fedora}
#fedora-config prep
cp %{SOURCE8} .
install -d $RPM_BUILD_ROOT%{gdesk}/switchdesk/
install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{gdesk}/switchdesk/Xclients.afterstep
install -d $RPM_BUILD_ROOT/etc/X11/gdm/Sessions/
install -m 0755 %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/gdm/Sessions/afterstep
install -d %{buildroot}%{gdesk}/xsessions/
install -m 0755 %{SOURCE6} %{buildroot}%{gdesk}/xsessions/afterstep.desktop
install -d %{buildroot}%{gdesk}/gnome/wm-properties/
install -m 0644 %{SOURCE7} %{buildroot}%{gdesk}/gnome/wm-properties/afterstep.desktop
rm -f %{buildroot}%{_datadir}/xsessions/AfterStep.desktop
rmdir %{buildroot}%{_datadir}/xsessions/
%endif
%if %{mdk}
# mandrake menu items
install -d $RPM_BUILD_ROOT/etc/X11/wmsession.d/
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/wmsession.d/42AfterStep
install -d $RPM_BUILD_ROOT/usr/lib/menu/afterstep
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/menu/afterstep
install -d $RPM_BUILD_ROOT/etc/menu-methods/
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT/etc/menu-methods/AfterStep
%endif
%if %{ismultiarch}
#mkdir -p %{buildroot}%{multiarch_bindir}
%multiarch_binaries %{buildroot}%{_bindir}/afterimage-config
%multiarch_binaries %{buildroot}%{_bindir}/afterimage-libs
%multiarch_binaries %{buildroot}%{_bindir}/afterstep-config
%multiarch_binaries %{buildroot}%{_bindir}/asgtk-config
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEW README* TEAM UPGRADE doc/languages doc/licences doc/code TODO doc/*.html
%doc src/ASDocGen/html/*html
%{_bindir}/*
%dir %{_datadir}/afterstep
%{_datadir}/afterstep/*
%{_mandir}/man1/*
# this is evil hack, but I can't get it to work otherwise on mdk
%if !%{fedora}
%config /etc/X11/wmsession.d/42AfterStep
/etc/menu-methods/AfterStep
%{_datadir}/xsessions/AfterStep.desktop
%config /usr/lib/menu/afterstep/AfterStep.menu
%endif
%if %{fedora}
/etc/X11/gdm/Sessions/afterstep
%{gdesk}/switchdesk/Xclients.afterstep
%{gdesk}/xsessions/afterstep.desktop
%{gdesk}/gnome/wm-properties/afterstep.desktop
%doc afterstep.fedora.README
%endif
%if %{generic}
%{__prefix}/xsessions/AfterStep.desktop
%endif

%files libs
%defattr(-,root,root)
%doc libAfterImage/README 
%{_libdir}/*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/libAfterBase
%dir %{_includedir}/libAfterConf
%dir %{_includedir}/libAfterImage
%dir %{_includedir}/libAfterStep
%dir %{_includedir}/libASGTK
%{_includedir}/libAfterBase/*
%{_includedir}/libAfterConf/*
%{_includedir}/libAfterImage/*
%{_includedir}/libAfterStep/*
%{_includedir}/libASGTK/*
%{_mandir}/man3/*
%doc src/ASDocGen/html/API/*html

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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
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
