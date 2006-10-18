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

%define prefix /usr
%define name bubblemon-dockapp
%define version 1.46
%define release 4

Summary: system monitoring dockapp based-on GNOME BubbleMon.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.ne.jp/asahi/linux/timecop/
Source0: http://www.ne.jp/asahi/linux/timecop/software/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdk}
Requires: libgtk+1.2-devel
%endif
%if %{fedora}
BuildRequires: gdk-pixbuf-devel
%endif

%description
This is a system monitoring dockapp, visually based on the GNOME
"BubbleMon" applet. Basically, it displays CPU and memory load as
bubbles in a jar of water. But that's where similarity ends. New
bubblemon-dockapp features translucent CPU load meter (for accurate
CPU load measurement), yellow duck swimming back and forth on the
water surface (just for fun), and fading load average and memory
usage screens. Either of the info screens can be locked to stay on
top of water/duck/cpu screen, so that you can see both statistics
at once. Pretty nifty toy for your desktop. Supports Linux, FreeBSD,
OpenBSD, and Solaris 2.6, 7 and 8. Code has been thoroughly
optimized since version 1.0, and even with all the features
compiled in, BubbleMon still uses very little CPU time. Load
Average screen locked at about 20% looks particularly sexy. All the
extra "bloated" features can be compiled out or disabled on
command-line, if you prefer original "BubbleMon" look.

%prep
%setup -q

%build
#./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 bubblemon $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc ChangeLog INSTALL README SUPPORTED_SYSTEMS doc/COPYING doc/Xdefaults.sample

%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.46-4
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.46-3
- changed prefix path to /usr.

* Sat Dec 17 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.46-2
- Added build require for fedora gdk-pixbuf-devel.

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.46-1
- Initial build.
