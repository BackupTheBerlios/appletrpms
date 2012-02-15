%define name		ascd
%define version		0.13.2
%define release		10%{?dist}

Summary:	Audio CD player applet/dockapp
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/applets/
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/ascd-0.13pr6-themes.tgz
Source2:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/dwing.tgz
Source3:	ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/lcd.tar.gz
Patch0:		ascd-0.13.2-ascdconfigure.patch
Patch1:		ascd-0.13.2-Imakefile.patch
Patch2:		ascd-0.13.2-copying-license.patch
Patch3:		ascd-0.13.2-5-debianbuild.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides:	ascd-themes
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	imake
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
A swallowable applet allows to control the CD-ROM and provides
the familiar controls like a regular CD player. In effect, this
is an advanced CD player with a fully customizable interface and
support for themes.

%prep
%setup -q -n ascd-%{version} -a 1

%patch0
%patch1
%patch2
%patch3

%build
./configure

make %{?_smp_mflags} \
	BINDIR=%{_bindir} \
	THEMESDIR=%{_datadir}/ascd

%install
rm -rf $RPM_BUILD_ROOT

cd ascd

make BINDIR=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT \
	THEMESDIR=%{_datadir}/ascd \
	install install.man

cd $RPM_BUILD_DIR/ascd-%{version}/ascd-0.13pr6-themes/

cp themes.tar $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

cd $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

tar xf themes.tar
tar xf dwing.tgz
tar xf lcd.tar.gz

rm -rf themes.tar
rm -rf dwing.tgz
rm -rf lcd.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING LICENSE README ascd/doc/CHANGES ascd/doc/NEWS
%{_bindir}/ascd
%{_datadir}/ascd/Default/back.xpm
%{_datadir}/ascd/Default/back_bar.xpm
%{_datadir}/ascd/Default/back_counter.xpm
%{_datadir}/ascd/Default/back_msg.xpm
%{_datadir}/ascd/Default/back_track.xpm
%{_datadir}/ascd/Default/bar.xpm
%{_datadir}/ascd/Default/cross.xpm
%{_datadir}/ascd/Default/digits.xpm
%{_datadir}/ascd/Default/digits2.xpm
%{_datadir}/ascd/Default/help.xpm
%{_datadir}/ascd/Default/panel.xpm
%{_datadir}/ascd/Themes/big/Theme
%{_datadir}/ascd/Themes/big/ascd.xpm
%{_datadir}/ascd/Themes/big/autoplay.xpm
%{_datadir}/ascd/Themes/big/autoplay_on.xpm
%{_datadir}/ascd/Themes/big/autorepeat.xpm
%{_datadir}/ascd/Themes/big/autorepeat_on.xpm
%{_datadir}/ascd/Themes/big/back.xpm
%{_datadir}/ascd/Themes/big/back_bar.xpm
%{_datadir}/ascd/Themes/big/back_bar2.xpm
%{_datadir}/ascd/Themes/big/back_buttons.xpm
%{_datadir}/ascd/Themes/big/back_counter.xpm
%{_datadir}/ascd/Themes/big/back_msg.xpm
%{_datadir}/ascd/Themes/big/back_track.xpm
%{_datadir}/ascd/Themes/big/bar.xpm
%{_datadir}/ascd/Themes/big/bar2.xpm
%{_datadir}/ascd/Themes/big/cross.xpm
%{_datadir}/ascd/Themes/big/disp.xpm
%{_datadir}/ascd/Themes/big/eject.xpm
%{_datadir}/ascd/Themes/big/fade.xpm
%{_datadir}/ascd/Themes/big/fwd.xpm
%{_datadir}/ascd/Themes/big/intro.xpm
%{_datadir}/ascd/Themes/big/intro_on.xpm
%{_datadir}/ascd/Themes/big/lend.xpm
%{_datadir}/ascd/Themes/big/lgo.xpm
%{_datadir}/ascd/Themes/big/lgo_on.xpm
%{_datadir}/ascd/Themes/big/lstart.xpm
%{_datadir}/ascd/Themes/big/options.xpm
%{_datadir}/ascd/Themes/big/options_on.xpm
%{_datadir}/ascd/Themes/big/panel.xpm
%{_datadir}/ascd/Themes/big/pause.xpm
%{_datadir}/ascd/Themes/big/pause_on.xpm
%{_datadir}/ascd/Themes/big/play.xpm
%{_datadir}/ascd/Themes/big/play_on.xpm
%{_datadir}/ascd/Themes/big/rew.xpm
%{_datadir}/ascd/Themes/big/small_play.xpm
%{_datadir}/ascd/Themes/big/stop.xpm
%{_datadir}/ascd/Themes/big/stop_on.xpm
%{_datadir}/ascd/Themes/big/theme.xpm
%{_datadir}/ascd/Themes/big/theme_on.xpm
%{_datadir}/ascd/Themes/big/upper.xpm
%{_datadir}/ascd/Themes/big/upper_on.xpm
%{_datadir}/ascd/Themes/big/wings.xpm
%{_datadir}/ascd/Themes/classic/Theme
%{_datadir}/ascd/Themes/classic/back.xpm
%{_datadir}/ascd/Themes/classic/back_counter.xpm
%{_datadir}/ascd/Themes/classic/back_track.xpm
%{_datadir}/ascd/Themes/classic/down.xpm
%{_datadir}/ascd/Themes/classic/eject.xpm
%{_datadir}/ascd/Themes/classic/pause.xpm
%{_datadir}/ascd/Themes/classic/play.xpm
%{_datadir}/ascd/Themes/classic/stop.xpm
%{_datadir}/ascd/Themes/classic/up.xpm
%{_datadir}/ascd/Themes/clean/Theme
%{_datadir}/ascd/Themes/clean/background.xpm
%{_datadir}/ascd/Themes/clean/bar.xpm
%{_datadir}/ascd/Themes/clean/digits.xpm
%{_datadir}/ascd/Themes/clean/digits2.xpm
%{_datadir}/ascd/Themes/clean/eject.xpm
%{_datadir}/ascd/Themes/clean/fade.xpm
%{_datadir}/ascd/Themes/clean/fwd.xpm
%{_datadir}/ascd/Themes/clean/intro.xpm
%{_datadir}/ascd/Themes/clean/intro_on.xpm
%{_datadir}/ascd/Themes/clean/lend.xpm
%{_datadir}/ascd/Themes/clean/lgo.xpm
%{_datadir}/ascd/Themes/clean/lgo_on.xpm
%{_datadir}/ascd/Themes/clean/lstart.xpm
%{_datadir}/ascd/Themes/clean/pause.xpm
%{_datadir}/ascd/Themes/clean/pause_on.xpm
%{_datadir}/ascd/Themes/clean/play.xpm
%{_datadir}/ascd/Themes/clean/play_on.xpm
%{_datadir}/ascd/Themes/clean/quit.xpm
%{_datadir}/ascd/Themes/clean/rdigits.xpm
%{_datadir}/ascd/Themes/clean/rew.xpm
%{_datadir}/ascd/Themes/clean/stop.xpm
%{_datadir}/ascd/Themes/default/Theme
%{_datadir}/ascd/Themes/default/autoplay.xpm
%{_datadir}/ascd/Themes/default/autoplay_on.xpm
%{_datadir}/ascd/Themes/default/autorepeat.xpm
%{_datadir}/ascd/Themes/default/autorepeat_on.xpm
%{_datadir}/ascd/Themes/default/eject.xpm
%{_datadir}/ascd/Themes/default/fade.xpm
%{_datadir}/ascd/Themes/default/fwd.xpm
%{_datadir}/ascd/Themes/default/intro.xpm
%{_datadir}/ascd/Themes/default/intro_on.xpm
%{_datadir}/ascd/Themes/default/lend.xpm
%{_datadir}/ascd/Themes/default/lgo.xpm
%{_datadir}/ascd/Themes/default/lgo_on.xpm
%{_datadir}/ascd/Themes/default/lstart.xpm
%{_datadir}/ascd/Themes/default/mixer2_back.xpm
%{_datadir}/ascd/Themes/default/mixer2_bar.xpm
%{_datadir}/ascd/Themes/default/mixer2_panel.xpm
%{_datadir}/ascd/Themes/default/mixer_back.xpm
%{_datadir}/ascd/Themes/default/mixer_bar.xpm
%{_datadir}/ascd/Themes/default/mixer_panel.xpm
%{_datadir}/ascd/Themes/default/options.xpm
%{_datadir}/ascd/Themes/default/options_on.xpm
%{_datadir}/ascd/Themes/default/pause.xpm
%{_datadir}/ascd/Themes/default/pause_on.xpm
%{_datadir}/ascd/Themes/default/play.xpm
%{_datadir}/ascd/Themes/default/play_on.xpm
%{_datadir}/ascd/Themes/default/quick/quick1.gif
%{_datadir}/ascd/Themes/default/quick/quick2.gif
%{_datadir}/ascd/Themes/default/rew.xpm
%{_datadir}/ascd/Themes/default/stop.xpm
%{_datadir}/ascd/Themes/default/stop_on.xpm
%{_datadir}/ascd/Themes/default/theme.xpm
%{_datadir}/ascd/Themes/default/theme_on.xpm
%{_datadir}/ascd/Themes/default/upper.xpm
%{_datadir}/ascd/Themes/default/upper_on.xpm
%{_datadir}/ascd/Themes/default/wings.xpm
%{_datadir}/ascd/Themes/dwing/Theme
%{_datadir}/ascd/Themes/dwing/ascd.xpm
%{_datadir}/ascd/Themes/dwing/back_counter.xpm
%{_datadir}/ascd/Themes/dwing/back_db.xpm
%{_datadir}/ascd/Themes/dwing/back_down.xpm
%{_datadir}/ascd/Themes/dwing/back_icon_center.xpm
%{_datadir}/ascd/Themes/dwing/back_icon_slider.xpm
%{_datadir}/ascd/Themes/dwing/back_track.xpm
%{_datadir}/ascd/Themes/dwing/back_up.xpm
%{_datadir}/ascd/Themes/dwing/digits.xpm
%{_datadir}/ascd/Themes/dwing/micons.xpm
%{_datadir}/ascd/Themes/dwing/mini_down.xpm
%{_datadir}/ascd/Themes/dwing/mini_eject.xpm
%{_datadir}/ascd/Themes/dwing/mini_pause.xpm
%{_datadir}/ascd/Themes/dwing/mini_pause_on.xpm
%{_datadir}/ascd/Themes/dwing/mini_play.xpm
%{_datadir}/ascd/Themes/dwing/mini_play_on.xpm
%{_datadir}/ascd/Themes/dwing/mini_stop.xpm
%{_datadir}/ascd/Themes/dwing/mini_up.xpm
%{_datadir}/ascd/Themes/dwing/mixer.xpm
%{_datadir}/ascd/Themes/dwing/plus.xpm
%{_datadir}/ascd/Themes/dwing/slider.xpm
%{_datadir}/ascd/Themes/dwing/slider2.xpm
%{_datadir}/ascd/Themes/dwing/vol2.xpm
%{_datadir}/ascd/Themes/dwing/volume.xpm
%{_datadir}/ascd/Themes/lcd/Theme
%{_datadir}/ascd/Themes/lcd/back.xpm
%{_datadir}/ascd/Themes/lcd/back_bar.xpm
%{_datadir}/ascd/Themes/lcd/back_counter.xpm
%{_datadir}/ascd/Themes/lcd/back_msg.xpm
%{_datadir}/ascd/Themes/lcd/back_track.xpm
%{_datadir}/ascd/Themes/lcd/bar.xpm
%{_datadir}/ascd/Themes/lcd/digits.xpm
%{_datadir}/ascd/Themes/lcd/eject.xpm
%{_datadir}/ascd/Themes/lcd/fade.xpm
%{_datadir}/ascd/Themes/lcd/fade_on.xpm
%{_datadir}/ascd/Themes/lcd/ffwd.xpm
%{_datadir}/ascd/Themes/lcd/intro.xpm
%{_datadir}/ascd/Themes/lcd/intro_on.xpm
%{_datadir}/ascd/Themes/lcd/pause.xpm
%{_datadir}/ascd/Themes/lcd/play.xpm
%{_datadir}/ascd/Themes/lcd/power.xpm
%{_datadir}/ascd/Themes/lcd/quick/quick1.gif
%{_datadir}/ascd/Themes/lcd/quick/quick2.gif
%{_datadir}/ascd/Themes/lcd/rewind.xpm
%{_datadir}/ascd/Themes/lcd/stop.xpm
%{_datadir}/ascd/Themes/orb/Theme
%{_datadir}/ascd/Themes/orb/back.xpm
%{_datadir}/ascd/Themes/orb/back_counter.xpm
%{_datadir}/ascd/Themes/orb/back_track.xpm
%{_datadir}/ascd/Themes/orb/digits.xpm
%{_datadir}/ascd/Themes/orb/down.xpm
%{_datadir}/ascd/Themes/orb/play.xpm
%{_datadir}/ascd/Themes/orb/play_on.xpm
%{_datadir}/ascd/Themes/orb/stop.xpm
%{_datadir}/ascd/Themes/orb/up.xpm
%{_datadir}/ascd/Themes/sands/Theme
%{_datadir}/ascd/Themes/sands/background.xpm
%{_datadir}/ascd/Themes/sands/bar.xpm
%{_datadir}/ascd/Themes/sands/digits.xpm
%{_datadir}/ascd/Themes/sands/digits2.xpm
%{_datadir}/ascd/Themes/sands/eject.xpm
%{_datadir}/ascd/Themes/sands/fade.xpm
%{_datadir}/ascd/Themes/sands/fwd.xpm
%{_datadir}/ascd/Themes/sands/intro.xpm
%{_datadir}/ascd/Themes/sands/intro_on.xpm
%{_datadir}/ascd/Themes/sands/lend.xpm
%{_datadir}/ascd/Themes/sands/lgo.xpm
%{_datadir}/ascd/Themes/sands/lgo_on.xpm
%{_datadir}/ascd/Themes/sands/lstart.xpm
%{_datadir}/ascd/Themes/sands/pause.xpm
%{_datadir}/ascd/Themes/sands/pause_on.xpm
%{_datadir}/ascd/Themes/sands/play.xpm
%{_datadir}/ascd/Themes/sands/play_on.xpm
%{_datadir}/ascd/Themes/sands/quit.xpm
%{_datadir}/ascd/Themes/sands/rew.xpm
%{_datadir}/ascd/Themes/sands/stop.xpm
%{_datadir}/ascd/Themes/tortured/Theme
%{_datadir}/ascd/Themes/tortured/ascd.xpm
%{_datadir}/ascd/Themes/tortured/back.xpm
%{_datadir}/ascd/Themes/tortured/back_counter.xpm
%{_datadir}/ascd/Themes/tortured/back_msg.xpm
%{_datadir}/ascd/Themes/tortured/back_track.xpm
%{_datadir}/ascd/Themes/tortured/bar.xpm
%{_datadir}/ascd/Themes/tortured/eject.xpm
%{_datadir}/ascd/Themes/tortured/eject_on.xpm
%{_datadir}/ascd/Themes/tortured/extension.xpm
%{_datadir}/ascd/Themes/tortured/extension3.xpm
%{_datadir}/ascd/Themes/tortured/loop.xpm
%{_datadir}/ascd/Themes/tortured/loop_end.xpm
%{_datadir}/ascd/Themes/tortured/loop_on.xpm
%{_datadir}/ascd/Themes/tortured/loop_start.xpm
%{_datadir}/ascd/Themes/tortured/mute.xpm
%{_datadir}/ascd/Themes/tortured/mute_on.xpm
%{_datadir}/ascd/Themes/tortured/next.xpm
%{_datadir}/ascd/Themes/tortured/panel.xpm
%{_datadir}/ascd/Themes/tortured/pause.xpm
%{_datadir}/ascd/Themes/tortured/pause_on.xpm
%{_datadir}/ascd/Themes/tortured/play.xpm
%{_datadir}/ascd/Themes/tortured/play_on.xpm
%{_datadir}/ascd/Themes/tortured/previous.xpm
%{_datadir}/ascd/Themes/tortured/stop.xpm
%{_datadir}/ascd/Themes/tortured/stop_on.xpm
%{_datadir}/ascd/Themes/tortured/volume.xpm
%{_datadir}/ascd/Themes/tortured/volume_back.xpm
%{_datadir}/ascd/Themes/vintage/Theme
%{_datadir}/ascd/Themes/vintage/back.xpm
%{_datadir}/ascd/Themes/vintage/bar.xpm
%{_datadir}/ascd/Themes/vintage/eject.xpm
%{_datadir}/ascd/Themes/vintage/fade.xpm
%{_datadir}/ascd/Themes/vintage/fwd.xpm
%{_datadir}/ascd/Themes/vintage/intro.xpm
%{_datadir}/ascd/Themes/vintage/intro_on.xpm
%{_datadir}/ascd/Themes/vintage/lend.xpm
%{_datadir}/ascd/Themes/vintage/lgo.xpm
%{_datadir}/ascd/Themes/vintage/lgo_on.xpm
%{_datadir}/ascd/Themes/vintage/lstart.xpm
%{_datadir}/ascd/Themes/vintage/pause.xpm
%{_datadir}/ascd/Themes/vintage/pause_on.xpm
%{_datadir}/ascd/Themes/vintage/play.xpm
%{_datadir}/ascd/Themes/vintage/play_on.xpm
%{_datadir}/ascd/Themes/vintage/quit.xpm
%{_datadir}/ascd/Themes/vintage/rew.xpm
%{_datadir}/ascd/Themes/vintage/stop.xpm
%{_datadir}/ascd/Themes/vintage/zob/digits.xpm
%{_datadir}/ascd/Themes/vintage/zob/digits2.xpm
%{_datadir}/ascd/Themes/wmcdplay/Theme
%{_datadir}/ascd/Themes/wmcdplay/back.xpm
%{_datadir}/ascd/Themes/wmcdplay/back_counter.xpm
%{_datadir}/ascd/Themes/wmcdplay/back_msg.xpm
%{_datadir}/ascd/Themes/wmcdplay/back_symbol.xpm
%{_datadir}/ascd/Themes/wmcdplay/back_track.xpm
%{_datadir}/ascd/Themes/wmcdplay/eject.xpm
%{_datadir}/ascd/Themes/wmcdplay/fwd.xpm
%{_datadir}/ascd/Themes/wmcdplay/next.xpm
%{_datadir}/ascd/Themes/wmcdplay/no_repeat.xpm
%{_datadir}/ascd/Themes/wmcdplay/pause.xpm
%{_datadir}/ascd/Themes/wmcdplay/play.xpm
%{_datadir}/ascd/Themes/wmcdplay/previous.xpm
%{_datadir}/ascd/Themes/wmcdplay/repeat.xpm
%{_datadir}/ascd/Themes/wmcdplay/rew.xpm
%{_datadir}/ascd/Themes/wmcdplay/stop.xpm
%{_datadir}/ascd/Themes/zinamp/Theme
%{_datadir}/ascd/Themes/zinamp/ascd.xpm
%{_datadir}/ascd/Themes/zinamp/autoplay.xpm
%{_datadir}/ascd/Themes/zinamp/autoplay_on.xpm
%{_datadir}/ascd/Themes/zinamp/autorepeat.xpm
%{_datadir}/ascd/Themes/zinamp/autorepeat_on.xpm
%{_datadir}/ascd/Themes/zinamp/back.xpm
%{_datadir}/ascd/Themes/zinamp/back_bar.xpm
%{_datadir}/ascd/Themes/zinamp/back_counter.xpm
%{_datadir}/ascd/Themes/zinamp/back_db.xpm
%{_datadir}/ascd/Themes/zinamp/back_icon_center.xpm
%{_datadir}/ascd/Themes/zinamp/back_icon_counter.xpm
%{_datadir}/ascd/Themes/zinamp/back_message.xpm
%{_datadir}/ascd/Themes/zinamp/back_track.xpm
%{_datadir}/ascd/Themes/zinamp/back_volume.xpm
%{_datadir}/ascd/Themes/zinamp/bar.xpm
%{_datadir}/ascd/Themes/zinamp/digits.xpm
%{_datadir}/ascd/Themes/zinamp/down.xpm
%{_datadir}/ascd/Themes/zinamp/eject.xpm
%{_datadir}/ascd/Themes/zinamp/intro.xpm
%{_datadir}/ascd/Themes/zinamp/intro_on.xpm
%{_datadir}/ascd/Themes/zinamp/l_end.xpm
%{_datadir}/ascd/Themes/zinamp/l_start.xpm
%{_datadir}/ascd/Themes/zinamp/loop.xpm
%{_datadir}/ascd/Themes/zinamp/loop_on.xpm
%{_datadir}/ascd/Themes/zinamp/mini_down.xpm
%{_datadir}/ascd/Themes/zinamp/mini_eject.xpm
%{_datadir}/ascd/Themes/zinamp/mini_pause.xpm
%{_datadir}/ascd/Themes/zinamp/mini_pause_on.xpm
%{_datadir}/ascd/Themes/zinamp/mini_play.xpm
%{_datadir}/ascd/Themes/zinamp/mini_play_on.xpm
%{_datadir}/ascd/Themes/zinamp/mini_stop.xpm
%{_datadir}/ascd/Themes/zinamp/mini_up.xpm
%{_datadir}/ascd/Themes/zinamp/mute.xpm
%{_datadir}/ascd/Themes/zinamp/mute_on.xpm
%{_datadir}/ascd/Themes/zinamp/next.xpm
%{_datadir}/ascd/Themes/zinamp/pause.xpm
%{_datadir}/ascd/Themes/zinamp/pause_on.xpm
%{_datadir}/ascd/Themes/zinamp/play.xpm
%{_datadir}/ascd/Themes/zinamp/play_on.xpm
%{_datadir}/ascd/Themes/zinamp/quit.xpm
%{_datadir}/ascd/Themes/zinamp/stop.xpm
%{_datadir}/ascd/Themes/zinamp/stop_on.xpm
%{_datadir}/ascd/Themes/zinamp/volume.xpm
%{_datadir}/ascd/Themes/zinamp/zob.gif
%{_datadir}/ascd/themes-manual.ps.gz
%{_mandir}/man1/ascd.*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-10
- added debian fix and build patches, added include patches.

* Wed Feb 03 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-9
- updated links for source files.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-8
- added distro info to release.

* Sat Mar 03 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-7
- merged ascd and ascd-themes; ascd-themes obsolete.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-6
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-5
- changed prefix path to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-4
- Changed Themes dir to /usr/X11R6/share/ascd/Themes.

* Sat Feb 27 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-3
- Changed tarball to that provided by tigr.net/afterstep/.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-2
- Changed themes from /usr/local/share to /usr/share.

* Mon Feb 07 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-1
- Initial build.
