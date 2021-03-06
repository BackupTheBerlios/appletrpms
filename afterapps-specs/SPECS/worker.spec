%define avftest	%(rpm -q --queryformat='%{VERSION}' avfs)
%define avfver	%avftest 
%define		name worker
%define		version 3.3.0
%define		release 1%{?dist}

Summary:	A file manager for the X Window System
Name:		%name
Version:	%version
Release:	%release
Epoch:		2
License:	GPLv2+
Group:		Applications/File
Source0:	http://www.boomerangsworld.de/cms/%{name}/downloads/%{name}-%{version}.tar.bz2
URL:		http://www.boomerangsworld.de/%{name}/
Requires:	avfs >= %{avftest}
Requires:	file-libs
Requires:	fuse
Requires:	glib2
Requires:	glibc
Requires:	libgcc
Requires:	libICE
Requires:	libSM
Requires:	libstdc++
Requires:	libX11
Requires:	libXft
Requires:	libXpm
BuildRequires:	avfs-devel
BuildRequires:	bzip2-devel
BuildRequires:	file-devel
BuildRequires:	gcc-c++
BuildRequires:	libX11-devel
BuildRequires:	libXft-devel
BuildRequires:	libXpm-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Worker is a file manager for the X Window System on UN*X.
The directories and files are shown in two independent panels

%prep
%setup -q

#Fix Man pages(UTF-8)
for f in ChangeLog man/fr/worker.1 man/it/worker.1; do
	iconv -f ISO-8859-1 -t UTF-8 $f > $f.new && \
	touch -r $f $f.new && \
	mv $f.new $f
done

%build
./configure --prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--enable-xft \
	--with-avfs \
	--with-libmagic \
	--without-hal \
	--with-dbus

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/

install -m 644 Icons/WorkerIcon16.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/worker.xpm
install -m 644 Icons/WorkerIcon32.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/worker.xpm
install -m 644 Icons/WorkerIcon48.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/worker.xpm
install -m 644 Icons/WorkerIcon.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/worker.xpm

rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/*.xpm

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=Worker File Manager
Comment=View and manage files
Exec=worker
Icon=worker.xpm
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                   \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category System						  \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README README_LARGEFILES THANKS
%{_bindir}/worker
%{_datadir}/applications/worker.desktop
%{_datadir}/icons/hicolor/*/apps/worker.xpm
%{_datadir}/worker/catalogs/*.catalog
%{_datadir}/worker/catalogs/*.catalog.coms
%{_datadir}/worker/catalogs/*.catalog.coms.utf8
%{_datadir}/worker/catalogs/*.catalog.flags
%{_datadir}/worker/catalogs/*.catalog.flags.utf8
%{_datadir}/worker/catalogs/*.catalog.utf8
%{_datadir}/worker/config-*
%{_datadir}/worker/hints-english
%{_datadir}/worker/hints-english.utf8
%{_datadir}/worker/scripts/displaywrapper_worker
%{_datadir}/worker/scripts/*.sh
%{_datadir}/worker/scripts/xeditor
%{_datadir}/worker/scripts/xliwrapper_worker
%{_mandir}/fr/man1/worker.*
%{_mandir}/it/man1/worker.*
%{_mandir}/man1/worker.*

%changelog
* Tue Jan 21 2014 J. Krebs <rpm_speedy@yahoo.com> 2:3.3.0-1
- new version.

* Mon Jun 24 2013 J. Krebs <rpm_speedy@yahoo.com> 2:3.0.0-1
- new version.

* Thu Nov 22 2012 J. Krebs <rpm_speedy@yahoo.com> 2:2.19.6-1
- new version.

* Fri Sep 07 2012 J. Krebs <rpm_speedy@yahoo.com> 2:2.19.5-1
- new version.

* Sat Apr 07 2012 J. Krebs <rpm_speedy@yahoo.com> 2:2.19.2-1
- new version.

* Mon Feb 20 2012 J. Krebs <rpm_speedy@yahoo.com> 2:2.19.1-1
- new version, memory leak fixed, enabled dbus.

* Tue Jan 31 2012 J. Krebs <rpm_speedy@yahoo.com> 2.19.0-2
- dbus has a memory leak, disabled with --without-dbus.

* Tue Jan 31 2012 J. Krebs <rpm_speedy@yahoo.com> 2.19.0-1
- new version.

* Sat Oct 01 2011 J. Krebs <rpm_speedy@yahoo.com> 2.18.1-1
- new version.

* Sat Jul 30 2011 J. Krebs <rpm_speedy@yahoo.com> 2.18.0-2
- Fedora is eliminating HAL. Let's remove it from worker. 

* Tue Jul 19 2011 J. Krebs <rpm_speedy@yahoo.com> 2.18.0-1
- new version.

* Thu Jun 02 2011 J. Krebs <rpm_speedy@yahoo.com> 2.17.13-1
- new version.

* Wed Mar 23 2011 J. Krebs <rpm_speedy@yahoo.com> 2.17.11-1
- new version.

* Tue Aug 31 2010 J. Krebs <rpm_speedy@yahoo.com> 2.17.9-1
- new version.

* Fri Jun 25 2010 J. Krebs <rpm_speedy@yahoo.com> 2.17.8-2
- new version, eliminated older documentation.

* Mon Mar 01 2010 J. Krebs <rpm_speedy@yahoo.com> 2.17.6-1
- new version

* Thu Nov 12 2009 J. Krebs <rpm_speedy@yahoo.com> 2.17.5-1
- new version

* Thu Jul 30 2009 J. Krebs <rpm_speedy@yahoo.com> 2.17.4-1
- new version

* Fri Jul 04 2008 J. Krebs <rpm_speedy@yahoo.com> 2.16.5-1
- new version

* Wed Jul 02 2008 J. Krebs <rpm_speedy@yahoo.com> 2.16.4-1
- new version

* Thu Apr 17 2008 J. Krebs <rpm_speedy@yahoo.com> 2.16.3-1
- new version

* Mon Feb 11 2008 J. Krebs <rpm_speedy@yahoo.com> 2.16.2-1
- new version

* Mon Dec 03 2007 J. Krebs <rpm_speedy@yahoo.com> 2.16.1-1
- new version

* Tue Nov 13 2007 J. Krebs <rpm_speedy@yahoo.com> 2.16.0-1
- new version

* Fri Jun 08 2007 J. Krebs <rpm_speedy@yahoo.com> 2.15.0-1
- new version

* Wed Apr 11 2007 J. Krebs <rpm_speedy@yahoo.com> 2.14.4-1
- new version

* Thu Sep 15 2006 J. Krebs <rpm_speedy@yahoo.com> 2.14.0-1
- new version

* Wed Nov 09 2005 J. Krebs <rpm_speedy@yahoo.com> 2.11.0-1
- new version

* Thu Jul 28 2005 J. Krebs <rpm_speedy@yahoo.com> 2.10.2-1
- new version

* Tue Jun 28 2005 J. Krebs <rpm_speedy@yahoo.com> 2.10.1-1
- new version

* Mon May 30 2005 J. Krebs <rpm_speedy@yahoo.com> 2.10.0-1
- new version

* Mon Feb 28 2005 J. Krebs <rpm_speedy@yahoo.com> 2.9.0-1
- new version
