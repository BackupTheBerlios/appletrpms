%define version 0.10.0
%define release 1%{?dist}
%define name	eina

Summary:	A classic player for a modern era
Name:		%name
Version:	%version
Release:	%release
License:	GPLv3
Group:		Applications/Multimedia
Source0:	http://launchpad.net/eina/trunk/%{version}/+download/%{name}-%{version}.tar.gz
URL:		http://eina.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	atk
Requires:	cairo
Requires:	cairo-gobject
Requires:	clutter
Requires:	clutter-gtk
Requires:	curl
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2 >= 2.28.0
Requires:	glibc
Requires:	gstreamer
Requires:	gtk3 >= 3.0.0
Requires:	json-glib
Requires:	libdrm
Requires:	libnotify
Requires:	libpng
Requires:	libuuid
Requires:	libX11
Requires:	libXcomposite
Requires:	libXdamage
Requires:	libXext
Requires:	libXfixes
Requires:	libxml2
Requires:	mesa-libGL
Requires:	pango
Requires:	sqlite
Requires:	unique

BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	cairo-gobject-devel
BuildRequires:	clutter-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	curl-devel
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 2.28.0
BuildRequires:	glibc-devel
BuildRequires:	gstreamer-devel 
BuildRequires:	gtk3-devel >= 3.0.0
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libdrm-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libuuid-devel
BuildRequires:	libX11-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel
BuildRequires:	redhat-rpm-config
BuildRequires:	sqlite-devel
BuildRequires:	unique-devel
BuildRequires:	vala
BuildRequires:	desktop-file-utils


%description
Eina works like a common portable music player. It just plays what you
want to listen to.

Apart from simplicity, today users expect more from a player than just
reading files. Artwork, lyrics, network support, artist data and other
music information find their right place in Eina.

Plugins can take care of all the extra functionality, since Eina exposes
everything from its internals. It's fairly easy to extend the player
capabilities and change the way it works inside. Feel free to request new
features and make things the way you like.

%package devel
Summary:    An Eina development environment
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Header files and libraries for building an extension library for Eina.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for eina.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang eina

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/gschemas.compiled

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/ldconfig
update-desktop-database &> /dev/null || :

%postun
/sbin/ldconfig
update-desktop-database &> /dev/null || :

if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f eina.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README
%attr(755, root, root) %{_libdir}/eina/lastfm/lastfmsubmitd/lastfmsubmitd
%{_bindir}/eina
%{_datadir}/applications/eina.desktop
%{_datadir}/eina/icons/hicolor/*/actions/bug.png
%{_datadir}/eina/icons/hicolor/*/actions/cover-default.png
%{_datadir}/eina/icons/hicolor/*/actions/cover-loading.png
%{_datadir}/eina/icons/hicolor/*/actions/loading-spin.gif
%{_datadir}/eina/icons/hicolor/*/actions/osx-status-icon.png
%{_datadir}/eina/icons/hicolor/*/actions/queue.png
%{_datadir}/eina/icons/hicolor/*/actions/random.png
%{_datadir}/eina/icons/hicolor/*/actions/repeat.png
%{_datadir}/eina/icons/hicolor/*/actions/standard-status-icon.png
%{_datadir}/eina/icons/hicolor/*/apps/eina.png
%{_datadir}/eina/icons/hicolor/*/apps/plugin.png
%{_datadir}/eina/icons/hicolor/scalable/actions/cover-default.svg
%{_datadir}/eina/icons/hicolor/scalable/actions/cover-loading.svg
%{_datadir}/eina/icons/hicolor/scalable/actions/random.svg
%{_datadir}/eina/icons/hicolor/scalable/actions/repeat.svg
%{_datadir}/eina/icons/hicolor/scalable/apps/eina.svg
%{_datadir}/eina/pixmaps/cover-default.png
%{_datadir}/eina/pixmaps/cover-loading.png
%{_datadir}/eina/pixmaps/cover-mask.png
%{_datadir}/eina/pixmaps/eina.svg
%{_datadir}/eina/pixmaps/loading-spin-16x16.gif
%{_datadir}/eina/pixmaps/plugin.png
%{_datadir}/glib-2.0/schemas/net.sourceforge.eina.gschema.xml
%{_libdir}/eina/adb/adb.ini
%{_libdir}/eina/adb/libadb.so
%{_libdir}/eina/art/art.ini
%{_libdir}/eina/art/libart.so
%{_libdir}/eina/clutty/clutty.ini
%{_libdir}/eina/clutty/libclutty.so
%{_libdir}/eina/dbus/dbus.ini
%{_libdir}/eina/dbus/libdbus.so
%{_libdir}/eina/dock/dock.ini
%{_libdir}/eina/dock/libdock.so
%{_libdir}/eina/fieshta/fieshta.ini
%{_libdir}/eina/fieshta/libfieshta.so
%{_libdir}/eina/lastfm/lastfm.ini
%{_libdir}/eina/lastfm/lastfm.png
%dir %{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/
%{_libdir}/eina/lastfm/lastfmsubmitd/COPYRIGHT
%{_libdir}/eina/lastfm/lastfmsubmitd/info.txt
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/client.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/client.pyc
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/client.pyo
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/config.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/config.pyc
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/config.pyo
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/__init__.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/__init__.pyc
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/__init__.pyo
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/marshaller.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/marshaller.pyc
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/marshaller.pyo
%{_libdir}/eina/lastfm/liblastfm.so
%{_libdir}/eina/lastfm/preferences.ui
%{_libdir}/eina/lomo/liblomo.so
%{_libdir}/eina/lomo/lomo.ini
%{_libdir}/eina/mpris/libmpris.so
%{_libdir}/eina/mpris/mpris.ini
%{_libdir}/eina/muine/libmuine.so
%{_libdir}/eina/muine/muine.ini
%{_libdir}/eina/ntfy/libntfy.so
%{_libdir}/eina/ntfy/ntfy.ini
%{_libdir}/eina/ntfy/ntfy.png
%{_libdir}/eina/player/libplayer.so
%{_libdir}/eina/player/player.ini
%{_libdir}/eina/player/preferences.ui
%{_libdir}/eina/playlist/libplaylist.so
%{_libdir}/eina/playlist/playlist.ini
%{_libdir}/eina/preferences/libpreferences.so
%{_libdir}/eina/preferences/preferences.ini
%{_libdir}/eina/statusicon/libstatusicon.so
%{_libdir}/eina/statusicon/statusicon.ini
%{_libdir}/libgel-1.1.so
%{_libdir}/libgel-1.1.so.0
%{_libdir}/libgel-1.1.so.0.1.1
%{_libdir}/libgel-ui-1.1.so
%{_libdir}/libgel-ui-1.1.so.0
%{_libdir}/libgel-ui-1.1.so.0.1.1
%{_libdir}/liblomo-1.1.so
%{_libdir}/liblomo-1.1.so.0
%{_libdir}/liblomo-1.1.so.0.1.1

%files devel
%defattr(-,root,root,-)
%{_includedir}/eina-0.10/eina/art/art.h
%{_includedir}/eina-0.10/eina/art/eina-art-backend.h
%{_includedir}/eina-0.10/eina/art/eina-art-search.h
%{_includedir}/eina-0.10/eina/art/eina-art.h
%{_includedir}/eina-0.10/eina/clutty/eina-cover-clutter.h
%{_includedir}/eina-0.10/eina/dock/dock.h
%{_includedir}/eina-0.10/eina/dock/eina-dock-tab.h
%{_includedir}/eina-0.10/eina/dock/eina-dock.h
%{_includedir}/eina-0.10/eina/eina-plugin.h
%{_includedir}/eina-0.10/eina/ext/curl-engine.h
%{_includedir}/eina-0.10/eina/ext/eina-application.h
%{_includedir}/eina-0.10/eina/ext/eina-file-chooser-dialog.h
%{_includedir}/eina-0.10/eina/ext/eina-file-utils.h
%{_includedir}/eina-0.10/eina/ext/eina-fs.h
%{_includedir}/eina-0.10/eina/ext/eina-stock.h
%{_includedir}/eina-0.10/eina/ext/eina-window.h
%{_includedir}/eina-0.10/eina/fieshta/eina-fiestha-behaviour.h
%{_includedir}/eina-0.10/eina/fieshta/fieshta.h
%{_includedir}/eina-0.10/eina/lomo/lomo.h
%{_includedir}/eina-0.10/eina/player/eina-cover-image.h
%{_includedir}/eina-0.10/eina/player/eina-cover.h
%{_includedir}/eina-0.10/eina/player/eina-player.h
%{_includedir}/eina-0.10/eina/player/eina-preferences-dialog.h
%{_includedir}/eina-0.10/eina/player/eina-preferences-tab.h
%{_includedir}/eina-0.10/eina/player/eina-seek.h
%{_includedir}/eina-0.10/eina/player/player.h
%{_includedir}/eina-0.10/eina/playlist/eina-playlist.h
%{_includedir}/eina-0.10/eina/playlist/playlist.h
%{_includedir}/gel-1.1/gel/gel-io-scanner.h
%{_includedir}/gel-1.1/gel/gel-io.h
%{_includedir}/gel-1.1/gel/gel-job-queue.h
%{_includedir}/gel-1.1/gel/gel-misc.h
%{_includedir}/gel-1.1/gel/gel-plugin-engine.h
%{_includedir}/gel-1.1/gel/gel-plugin-info.h
%{_includedir}/gel-1.1/gel/gel-plugin.h
%{_includedir}/gel-1.1/gel/gel-str-parser.h
%{_includedir}/gel-1.1/gel/gel-string.h
%{_includedir}/gel-1.1/gel/gel-ui-dialogs.h
%{_includedir}/gel-1.1/gel/gel-ui-generic.h
%{_includedir}/gel-1.1/gel/gel-ui-plugin-manager.h
%{_includedir}/gel-1.1/gel/gel-ui-scale.h
%{_includedir}/gel-1.1/gel/gel-ui-utils.h
%{_includedir}/gel-1.1/gel/gel-ui.h
%{_includedir}/gel-1.1/gel/gel.h
%{_includedir}/lomo-1.1/lomo/lomo-metadata-parser.h
%{_includedir}/lomo-1.1/lomo/lomo-player.h
%{_includedir}/lomo-1.1/lomo/lomo-stream.h
%{_includedir}/lomo-1.1/lomo/lomo-util.h
%{_includedir}/lomo-1.1/lomo/lomo.h
%{_libdir}/pkgconfig/eina-0.10.pc
%{_libdir}/pkgconfig/gel-1.1.pc
%{_libdir}/pkgconfig/gel-ui-1.1.pc
%{_libdir}/pkgconfig/lomo-1.1.pc

%files doc
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/eina/api-index-full.html
%{_datadir}/gtk-doc/html/eina/ch01.html
%{_datadir}/gtk-doc/html/eina/deprecated-api-index.html
%{_datadir}/gtk-doc/html/eina/EinaApplication.html
%{_datadir}/gtk-doc/html/eina/eina-curl-engine.html
%{_datadir}/gtk-doc/html/eina/eina.devhelp
%{_datadir}/gtk-doc/html/eina/eina.devhelp2
%{_datadir}/gtk-doc/html/eina/eina-eina-file-utils.html
%{_datadir}/gtk-doc/html/eina/eina-eina-fs.html
%{_datadir}/gtk-doc/html/eina/eina-eina-stock.html
%{_datadir}/gtk-doc/html/eina/EinaFileChooserDialog.html
%{_datadir}/gtk-doc/html/eina/EinaWindow.html
%{_datadir}/gtk-doc/html/eina/home.png
%{_datadir}/gtk-doc/html/eina/index.html
%{_datadir}/gtk-doc/html/eina/index.sgml
%{_datadir}/gtk-doc/html/eina/left.png
%{_datadir}/gtk-doc/html/eina/object-tree.html
%{_datadir}/gtk-doc/html/eina/right.png
%{_datadir}/gtk-doc/html/eina/style.css
%{_datadir}/gtk-doc/html/eina/up.png
%{_datadir}/gtk-doc/html/gel/annotation-glossary.html
%{_datadir}/gtk-doc/html/gel/api-index-full.html
%{_datadir}/gtk-doc/html/gel/ch01.html
%{_datadir}/gtk-doc/html/gel/deprecated-api-index.html
%{_datadir}/gtk-doc/html/gel/gel.devhelp
%{_datadir}/gtk-doc/html/gel/gel.devhelp2
%{_datadir}/gtk-doc/html/gel/gel-gel-misc.html
%{_datadir}/gtk-doc/html/gel/gel-gel-plugin.html
%{_datadir}/gtk-doc/html/gel/gel-gel-plugin-info.html
%{_datadir}/gtk-doc/html/gel/gel-gel-string.html
%{_datadir}/gtk-doc/html/gel/gel-gel-str-parser.html
%{_datadir}/gtk-doc/html/gel/gel-gel-ui-dialogs.html
%{_datadir}/gtk-doc/html/gel/gel-gel-ui-utils.html
%{_datadir}/gtk-doc/html/gel/GelIOScanner.html
%{_datadir}/gtk-doc/html/gel/GelJobQueue.html
%{_datadir}/gtk-doc/html/gel/GelPluginEngine.html
%{_datadir}/gtk-doc/html/gel/GelUIGeneric.html
%{_datadir}/gtk-doc/html/gel/GelUIPluginManager.html
%{_datadir}/gtk-doc/html/gel/home.png
%{_datadir}/gtk-doc/html/gel/index.html
%{_datadir}/gtk-doc/html/gel/index.sgml
%{_datadir}/gtk-doc/html/gel/left.png
%{_datadir}/gtk-doc/html/gel/object-tree.html
%{_datadir}/gtk-doc/html/gel/right.png
%{_datadir}/gtk-doc/html/gel/style.css
%{_datadir}/gtk-doc/html/gel/up.png
%dir %{_datadir}/gtk-doc/html/lomo
%{_datadir}/gtk-doc/html/lomo/annotation-glossary.html
%{_datadir}/gtk-doc/html/lomo/api-index-full.html
%{_datadir}/gtk-doc/html/lomo/ch01.html
%{_datadir}/gtk-doc/html/lomo/deprecated-api-index.html
%{_datadir}/gtk-doc/html/lomo/home.png
%{_datadir}/gtk-doc/html/lomo/index.html
%{_datadir}/gtk-doc/html/lomo/index.sgml
%{_datadir}/gtk-doc/html/lomo/left.png
%{_datadir}/gtk-doc/html/lomo/lomo.devhelp
%{_datadir}/gtk-doc/html/lomo/lomo.devhelp2
%{_datadir}/gtk-doc/html/lomo/lomo-lomo-stats.html
%{_datadir}/gtk-doc/html/lomo/lomo-lomo-util.html
%{_datadir}/gtk-doc/html/lomo/LomoMetadataParser.html
%{_datadir}/gtk-doc/html/lomo/LomoPlayer.html
%{_datadir}/gtk-doc/html/lomo/LomoStream.html
%{_datadir}/gtk-doc/html/lomo/object-tree.html
%{_datadir}/gtk-doc/html/lomo/right.png
%{_datadir}/gtk-doc/html/lomo/style.css
%{_datadir}/gtk-doc/html/lomo/up.png

%changelog
* Sun Jun 12 2011 J. Krebs <rpm_speedy@yahoo.com> 0.10.0-1
- new version.

* Sat May 29 2010 J. Krebs <rpm_speedy@yahoo.com> 0.9.3-1
- initial build.

