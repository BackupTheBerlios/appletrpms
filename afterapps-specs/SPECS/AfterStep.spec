%define	name	AfterStep
%define	fver	2.00.02
%define	version	2.00.02
%define	release	3
%define	prefix	/usr/X11R6

Summary:	AfterStep Window Manager (NeXTalike)
Name:		%{name}
Version:	%{version}
Release:	%{release}
Copyright:	GPL
Group:		User Interface/Desktops
URL:		http://www.afterstep.org
Vendor:		The AfterStep Team (see TEAM in docdir)
Source:		ftp://ftp.afterstep.org/stable/%{name}-%{fver}.tar.gz
Distribution:	The AfterStep TEAM
Packager:	Sean Dague <sean at dague dot net>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires: %{name}-libs qiv

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
copyright:	GPL
group:		User Interface/Desktops

%description libs
  Libraries neeeded by AfterStep 2.0

%package devel
summary:	AftterStep libs include files
version:	%{version}
release:	%{release}
copyright:	GPL
group:		User Interface/Desktops
Requires: %{name}-libs

%description devel
  AftterStep libs include files

%prep
%setup -q -n %{name}-%{fver}
#%patch0 -p1

# RedHat's version of the startmenu
# rm -rf afterstep/start
# tar xzf $RPM_SOURCE_DIR/AfterStep-redhat.tar.gz

CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=%{prefix} --datadir=%{prefix}/share \
    --disable-staticlibs --enable-sharedlibs \
	--with-helpcommand="aterm -e man" \
	--with-desktops=1 --with-deskgeometry=2x3 \
        --with-imageloader="qiv --root"

%build
make

if [[ -x /usr/bin/sgml2html ]]; then sgml2html doc/afterstep.sgml; fi
cd src/ASDocGen && ./ASDocGen -l log.html -t html && cd ../..

%install
if [[ -d $RPM_BUILD_ROOT ]]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install
rm -f $RPM_BUILD_ROOT%{prefix}/bin/{sessreg,xpmroot}
for f in libAfter{Base,Conf,Image,Step}; do
   cp -a $f/$f.so* %{buildroot}%{prefix}/lib
done
# add desktop files
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
install -m 644 AfterStep.desktop.final $RPM_BUILD_ROOT/usr/share/applications/AfterStep.desktop
mkdir -p $RPM_BUILD_ROOT/usr/share/gnome/wm-properties
install -m 644 AfterStep.desktop.final $RPM_BUILD_ROOT/usr/share/gnome/wm-properties/AfterStep.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEW README* TEAM UPGRADE doc/languages doc/licences doc/code TODO doc/*.html
%{prefix}/bin/*
%dir %{prefix}/share/afterstep
%config %{prefix}/share/afterstep/*
%config /usr/share/gnome/wm-properties/AfterStep.desktop
%config /usr/share/applications/AfterStep.desktop
%config /usr/X11R6/share/xsessions/AfterStep.desktop

%files libs
%defattr(-,root,root)
%doc libAfterImage/README src/ASDocGen/html/*
%{prefix}/lib/*
%{prefix}/man/*/*

%files devel
%defattr(-,root,root)
%dir %{prefix}/include/libAfterBase
%dir %{prefix}/include/libAfterConf
%dir %{prefix}/include/libAfterImage
%dir %{prefix}/include/libAfterStep
%{prefix}/include/libAfterBase/*
%{prefix}/include/libAfterConf/*
%{prefix}/include/libAfterImage/*
%{prefix}/include/libAfterStep/*


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
* Sat Feb 26 2005 Sean Dague <sean@dague.net> 2.00.02-2
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

