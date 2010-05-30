%define version 0.9.3
%define release 1%{?dist}
%define name	eina

Summary:	A classic player for a modern era
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/Multimedia
Source0:	http://launchpad.net/eina/trunk/0.9.3/+download/%{name}-%{version}.tar.gz
URL:		http://eina.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	gstreamer curl gtk2 unique sqlite libuuid libnotify clutter-gtk atk
Requires:	freetype gdk-pixbuf dbus-glib pango cairo libnotify glibc libxml2
BuildRequires:	freetype-devel
BuildRequires:	gstreamer-devel 
BuildRequires:	intltool 
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	unique-devel
BuildRequires:	sqlite-devel
BuildRequires:	desktop-file-utils
BuildRequires:	curl-devel
BuildRequires:	libnotify-devel
BuildRequires:	libuuid-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	atk-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	pango-devel
BuildRequires:	cairo-devel
BuildRequires:	libnotify-devel
BuildRequires:	glibc-devel
BuildRequires:	libxml2-devel

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

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/ldconfig
update-desktop-database &> /dev/null || :

%postun
/sbin/ldconfig
update-desktop-database &> /dev/null || :

%files -f eina.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/eina
%{_bindir}/vogon
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
%{_datadir}/eina/ui/dock.ui
%{_datadir}/eina/ui/log.ui
%{_datadir}/eina/ui/player-preferences.ui
%{_datadir}/eina/ui/player.ui
%{_datadir}/eina/ui/playlist.ui
%{_datadir}/eina/ui/plugins.ui
%{_libdir}/libgel-1.0.so.1
%{_libdir}/libgel-1.0.so.1.0.0
%{_libdir}/liblomo-1.0.so.1
%{_libdir}/liblomo-1.0.so.1.0.0
%{_libdir}/eina/adb/adb.png
%{_libdir}/eina/adb/libadb.so
%{_libdir}/eina/callhome/libcallhome.so
%{_libdir}/eina/coverplus/libcoverplus.so
%{_libdir}/eina/lastfm/lastfm.png
%{_libdir}/eina/lastfm/lastfm.ui
%{_libdir}/eina/lastfm/liblastfm.so
%{_libdir}/eina/lastfm/logo.gif
%{_libdir}/eina/lastfm/lastfmsubmitd/COPYRIGHT
%{_libdir}/eina/lastfm/lastfmsubmitd/info.txt
%attr(755, root, root) %{_libdir}/eina/lastfm/lastfmsubmitd/lastfmsubmitd
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/__init__.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/client.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/config.py
%{_libdir}/eina/lastfm/lastfmsubmitd/lastfm/marshaller.py
%{_libdir}/eina/muine/libmuine.so
%{_libdir}/eina/muine/muine.ui
%{_libdir}/eina/ntfy/libntfy.so
%{_libdir}/eina/ntfy/ntfy.png
%{_libdir}/eina/recently/dock.ui
%{_libdir}/eina/recently/go-back.png

%files devel
%defattr(-,root,root,-)
%{_includedir}/eina-0.9/eina/art.h
%{_includedir}/eina-0.9/eina/eina-obj.h
%{_includedir}/eina-0.9/eina/eina-plugin.h
%{_includedir}/eina-0.9/eina/fs.h
%{_includedir}/eina-0.9/eina/lomo.h
%{_includedir}/eina-0.9/eina/preferences.h
%{_includedir}/eina-0.9/eina/settings.h
%{_includedir}/eina-0.9/eina/window.h
%{_includedir}/eina-0.9/eina/ext/curl-engine.h
%{_includedir}/eina-0.9/eina/ext/eina-conf.h
%{_includedir}/eina-0.9/eina/ext/eina-cover.h
%{_includedir}/eina-0.9/eina/ext/eina-cover-clutter.h
%{_includedir}/eina-0.9/eina/ext/eina-cover-image.h
%{_includedir}/eina-0.9/eina/ext/eina-file-chooser-dialog.h
%{_includedir}/eina-0.9/eina/ext/eina-file-utils.h
%{_includedir}/eina-0.9/eina/ext/eina-plugin-dialog.h
%{_includedir}/eina-0.9/eina/ext/eina-plugin-properties.h
%{_includedir}/eina-0.9/eina/ext/eina-preferences-dialog.h
%{_includedir}/eina-0.9/eina/ext/eina-seek.h
%{_includedir}/eina-0.9/eina/ext/eina-stock.h
%{_includedir}/eina-0.9/eina/ext/eina-volume.h
%{_includedir}/eina-0.9/eina/ext/eina-window.h
%{_includedir}/eina-0.9/gel/gel-app.h
%{_includedir}/eina-0.9/gel/gel.h
%{_includedir}/eina-0.9/gel/gel-io.h
%{_includedir}/eina-0.9/gel/gel-io-misc.h
%{_includedir}/eina-0.9/gel/gel-io-op-result.h
%{_includedir}/eina-0.9/gel/gel-io-ops.h
%{_includedir}/eina-0.9/gel/gel-io-recurse-tree.h
%{_includedir}/eina-0.9/gel/gel-io-scanner.h
%{_includedir}/eina-0.9/gel/gel-io-tree.h
%{_includedir}/eina-0.9/gel/gel-job-queue.h
%{_includedir}/eina-0.9/gel/gel-misc.h
%{_includedir}/eina-0.9/gel/gel-plugin.h
%{_includedir}/eina-0.9/gel/gel-string.h
%{_includedir}/eina-0.9/gel/gel-str-parser.h
%{_includedir}/eina-0.9/gel/gel-ui.h
%{_includedir}/eina-0.9/lomo/lomo-metadata-parser.h
%{_includedir}/eina-0.9/lomo/lomo-player.h
%{_includedir}/eina-0.9/lomo/lomo-stream.h
%{_includedir}/eina-0.9/lomo/lomo-util.h
%{_includedir}/eina-0.9/plugins/adb/adb.h
%{_libdir}/libgel-1.0.so
%{_libdir}/liblomo-1.0.so
%{_libdir}/pkgconfig/eina-0.9.pc

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/gtk-doc/html/lomo
%{_datadir}/gtk-doc/html/lomo/api-index-full.html
%{_datadir}/gtk-doc/html/lomo/ch01.html
%{_datadir}/gtk-doc/html/lomo/home.png
%{_datadir}/gtk-doc/html/lomo/index.html
%{_datadir}/gtk-doc/html/lomo/index.sgml
%{_datadir}/gtk-doc/html/lomo/left.png
%{_datadir}/gtk-doc/html/lomo/lomo.devhelp
%{_datadir}/gtk-doc/html/lomo/lomo.devhelp2
%{_datadir}/gtk-doc/html/lomo/lomo-lomo-util.html
%{_datadir}/gtk-doc/html/lomo/LomoMetadataParser.html
%{_datadir}/gtk-doc/html/lomo/LomoPlayer.html
%{_datadir}/gtk-doc/html/lomo/LomoStream.html
%{_datadir}/gtk-doc/html/lomo/object-tree.html
%{_datadir}/gtk-doc/html/lomo/right.png
%{_datadir}/gtk-doc/html/lomo/style.css
%{_datadir}/gtk-doc/html/lomo/up.png

%changelog
* Sat May 29 2010 J. Krebs <rpm_speedy@yahoo.com> 0.9.3-1
- initial build.

