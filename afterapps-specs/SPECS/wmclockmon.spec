### BEGIN Distro Defines
%define mdk  %(if [ -e /etc/mandrake-release ]; then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

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
%endif

%if %{suse}
  %define generic 0
%endif
### END Distro Definitions

%define		name wmclockmon
%define		version 0.8.1
%define		release 7%{?dist}

Summary:	digital clock with 7 different styles in either LCD or LED style
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://tnemeth.free.fr/projets/dockapps.html
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-gtk2.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	glibc
Requires:	libpng
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	pango
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	pango-devel

%if %{mdk}
Requires:	libgtk+2.0_0
Buildrequires:	libgtk+2.0_0-devel
%endif

%if %{fedora}
Requires:	gtk2
BuildRequires:	gtk2-devel
%endif

%description
wmclockmon is a nice digital clock with 7 different styles in either
LCD or LED style; uses locales to display weekday and month names.
It also features the internet time.
Includes wmclockmon-cal, a calendar display and wmclockmon-config,
a configuration tool for the package.

%prep
%setup -q
%patch0

%build
#autoreconf -i
#automake-1.4 --add-missing

./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wmclockmon/

rm -rf styles/Makefile*

install -m 644 styles/* $RPM_BUILD_ROOT%{_datadir}/wmclockmon/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/sample*.wmclockmonrc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/wmclockmon
%{_bindir}/wmclockmon-cal
%{_bindir}/wmclockmon-config
%{_datadir}/wmclockmon/backlight_0_color_off.xpm
%{_datadir}/wmclockmon/backlight_0_color_on.xpm
%{_datadir}/wmclockmon/backlight0_off.xpm
%{_datadir}/wmclockmon/backlight0_on.xpm
%{_datadir}/wmclockmon/backlight_1_color_off.xpm
%{_datadir}/wmclockmon/backlight_1_color_on.xpm
%{_datadir}/wmclockmon/backlight1_off.xpm
%{_datadir}/wmclockmon/backlight1_on.xpm
%{_datadir}/wmclockmon/backlight_2_color_off.xpm
%{_datadir}/wmclockmon/backlight_2_color_on.xpm
%{_datadir}/wmclockmon/backlight2_off.xpm
%{_datadir}/wmclockmon/backlight2_on.xpm
%{_datadir}/wmclockmon/backlight_3_color_off.xpm
%{_datadir}/wmclockmon/backlight_3_color_on.xpm
%{_datadir}/wmclockmon/backlight3_off.xpm
%{_datadir}/wmclockmon/backlight3_on.xpm
%{_datadir}/wmclockmon/backlight_4_color_off.xpm
%{_datadir}/wmclockmon/backlight_4_color_on.xpm
%{_datadir}/wmclockmon/backlight4_off.xpm
%{_datadir}/wmclockmon/backlight4_on.xpm
%{_datadir}/wmclockmon/backlight_5_color_off.xpm
%{_datadir}/wmclockmon/backlight_5_color_on.xpm
%{_datadir}/wmclockmon/backlight5_off.xpm
%{_datadir}/wmclockmon/backlight5_on.xpm
%{_datadir}/wmclockmon/backlight_6_color_off.xpm
%{_datadir}/wmclockmon/backlight_6_color_on.xpm
%{_datadir}/wmclockmon/backlight6_off.xpm
%{_datadir}/wmclockmon/backlight6_on.xpm
%{_datadir}/wmclockmon/backlightB_color_off.xpm
%{_datadir}/wmclockmon/backlightB_color_on.xpm
%{_datadir}/wmclockmon/backlightB_new_off.xpm
%{_datadir}/wmclockmon/backlightB_new_on.xpm
%{_datadir}/wmclockmon/backlightB_off.xpm
%{_datadir}/wmclockmon/backlightB_old_off.xpm
%{_datadir}/wmclockmon/backlightB_old_on.xpm
%{_datadir}/wmclockmon/backlightB_on.xpm
%{_datadir}/wmclockmon/backlightI_color_off.xpm
%{_datadir}/wmclockmon/backlightI_color_on.xpm
%{_datadir}/wmclockmon/backlightI_off.xpm
%{_datadir}/wmclockmon/backlightI_on.xpm
%{_datadir}/wmclockmon/default.bwcs
%{_datadir}/wmclockmon/default.iwcs
%{_datadir}/wmclockmon/default.lwcs
%{_datadir}/wmclockmon/default.mwcs
%{_datadir}/wmclockmon/default.pwcs
%{_datadir}/wmclockmon/lcd1.mwcs
%{_datadir}/wmclockmon/lcd2.mwcs
%{_datadir}/wmclockmon/lcd3.mwcs
%{_datadir}/wmclockmon/lcd4.mwcs
%{_datadir}/wmclockmon/lcd5.mwcs
%{_datadir}/wmclockmon/lcd6.mwcs
%{_datadir}/wmclockmon/led0.mwcs
%{_datadir}/wmclockmon/led1.mwcs
%{_datadir}/wmclockmon/led2.mwcs
%{_datadir}/wmclockmon/led3.mwcs
%{_datadir}/wmclockmon/led4.mwcs
%{_datadir}/wmclockmon/led5.mwcs
%{_datadir}/wmclockmon/led6.mwcs
%{_datadir}/wmclockmon/led.bwcs
%{_datadir}/wmclockmon/led.iwcs
%{_datadir}/wmclockmon/led.lwcs
%{_datadir}/wmclockmon/led.pwcs
%{_datadir}/wmclockmon/letters_color.xpm
%{_datadir}/wmclockmon/letters_new.xpm
%{_datadir}/wmclockmon/letters.xpm
%{_datadir}/wmclockmon/new.bwcs
%{_datadir}/wmclockmon/new.lwcs
%{_datadir}/wmclockmon/new.mwcs
%{_datadir}/wmclockmon/new.pwcs
%{_datadir}/wmclockmon/parts_color.xpm
%{_datadir}/wmclockmon/parts_new.xpm
%{_datadir}/wmclockmon/parts.xpm
%{_mandir}/man1/wmclockmon.1.gz
%{_mandir}/man1/wmclockmon-cal.1.gz
%{_mandir}/man1/wmclockmon-config.1.gz

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-7
- added gtk2 patch from gentoo, updated SPEC file.

* Wed Oct 19 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-6
- cleanup.

* Fri Jun 15 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-5
- added require for gtk+-devel, gtk+.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-2
- changed prefix path to /usr.

* Sun Apr 10 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.1-1
- Updated to 0.8.1.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-2
- Changed styles dir to /usr/X11R6/share from /usr/share.

* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-1
- Initial build.

