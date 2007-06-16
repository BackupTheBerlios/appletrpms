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

%define name wmfishtime
%define version 1.24
%define release 5%{?dist}

Summary: clock dockapp with fish
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.ne.jp/asahi/linux/timecop/
Source0: http://www.ne.jp/asahi/linux/timecop/software/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if %{mdk}
Requires: libgtk+1.2
Buildrequires: libgtk+1.2-devel
%endif
%if %{fedora}
Requires: gtk+
Requires: gdk-pixbuf
BuildRequires: gtk+-devel
BuildRequires: gdk-pixbuf-devel
%endif

%description
Well, this is just your standard time dockapp. Top part has the clock face,
bottom part has day of the week, followed by day, followed by month. Yellow
hand counts seconds, green hand counts minutes, red hand counts hours. Few
seconds after startup there are at least 32 bubbles floating up behind the
clock face.  There are 4 fishes randomly swimming back and forth. If you move
your mouse inside the dockapp window, the fish will get scared and run away.
If you compiled in mail checking (default), then whenever you get new mail
in the file pointed to by the $MAIL variable, it will display green weed
partially blocking the day/month counter, to remind you to read your mail.
If $MAIL is not set, nothing happens.

%prep
%setup -q

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 wmfishtime $RPM_BUILD_ROOT%{_bindir}/
install -m 644 wmfishtime.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc ALL_I_GET_IS_A_GRAY_BOX AUTHORS CODING COPYING ChangeLog INSTALL README


%changelog
* Fri Jun 15 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.24-5
- added require for gtk+-devel, gtk+.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.24-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.24-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.24-2
- changed prefix path to /usr.

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.24-1
- Initial build.
