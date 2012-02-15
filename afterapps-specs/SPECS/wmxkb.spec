%define		name wmxkb
%define		version 1.2.2
%define		release 10%{?dist}

Summary:	A dockable/swallowed XKB groups indicator and switch
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/221
Source0:	http://dockapps.windowmaker.org/download.php/id/487/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
%{name} showns and controls XKB groups (XFree86 key maps)
It can be used as a dockable/swallowed applet with Window Maker or any window
manager that supports swallowing, including gnome, afterstep, fvwm and clones.
Alternatively, you can run %{name} as a normal window with any window manager. 
With %{name} you can also set additional (e.g. multimedia) keys for switching
groups, or setting a particular group. You can also assign a shell script to
run whenever a particular group is activated.

%prep
%setup -q

%build
./configure --with-rpm --prefix=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make BINDIR=$RPM_BUILD_ROOT%{_bindir} install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/wmxkb/
install -m 644 pixmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/wmxkb/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/pixmaps/wmxkb
%doc COPYING README manual.html WMxkb_flexy WMxkb_nonflexy

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-10
- shifted URLs to http://dockapps.windowmaker.org.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-9
- updated URL info to dockapps.org.

* Thu Aug 06 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-8
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-7
- added distro info to release.

* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-6
- spec file cleanup.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-5
- Updated Source path.

* Mon Mar 20 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-4
- changed prefix pat to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-3
- changed pixmaps to /usr/X11R6/share/pixmaps/wmxkb.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-2
- src.rpm script barfed under Fedora. Tweaked it.

* Thu Jun 17 2004 Michael Glickman <wmalms@yahoo.com>
- v 1.2.2
- Bug fixes: image selection with flexy group
-            no crash if too many groups are defined
-            fixed RPM installation script

* Tue Feb 03 2004 Michael Glickman <wmalms@yahoo.com>
- v 1.2.1
- Minor bug fix: eliminate colon(:) from symbol names
- Default docking with PWM 

* Wed Dec 10 2003 Michael Glickman <wmalms@yahoo.com>
- v 1.2.0
- Support for group-specific images (e.g.country flags)
- Custom background images

* Wed Oct 29 2003 Michael Glickman <wmalms@yahoo.com>
- v 1.1.0
- Support for BlackBox and clones
- Extended windowMode option
- IconTitle (-ititle) parameter
- A neater xkb bug work arround (thanks to Ivan Pascal)

* Fri Oct 10 2003 Michael Glickman <wmalms@yahoo.com>
- RPM release



