### BEGIN Distro Defines
### mdk, fedora, suse & generic are distros
### mandriva, fedoragcc4, and susegcc4 define gcc 4.0 compilers
%define mdk  %(if [ -e /etc/mandrake-release -o -e /etc/mandriva-release]; then echo 1; else echo 0; fi;)
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
### END Distro Definitions


%define prefix /usr/X11R6
%define name wmcalendar
%define version 0.5.0
%define release 2

Summary: wmCalendar is a calendar dockapp.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sourceforge.net/projects/wmcalendar/
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.ogo2ical
Patch0: %{name}-%{version}.wharf.patch
Patch1: %{name}-%{version}-mallocfix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: libical
Requires: libical

%description
wmCalendar is a calendar dockapp that provides the following:
- monthly view
- gregorian, islamic, and persian calendar
- english and farsi names and numbers
- utf8 support
- change month with mousewheel or click on button
- highlight current date
- interface to iCalendar data(Ximian Evolution, Mozilla Calendar,
  KOrganizer, ...)
- mark days as free or busy
- launch external calendar program
- show moonphase
- popup detail information about calendar-entries
- variable startday of week

Includes the script "ogo2ical" that extracts appointments from
OpenGroupware and converts them to iCalendar format for use in
wmCalendar.  Many thanks to Daniel Tschan for his script!

%prep
%setup -q
%patch0
%patch1

cp %{SOURCE1} ogo2ical

%build
cd Src

if [ %{fedoragcc4} -eq 1 ]; then make CC=gcc32; \
	elif [ %{susegcc4} -eq 1 ]; then make CC=gcc33; \
	else make; \
fi;

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
install -s -m 755 Src/wmCalendar $RPM_BUILD_ROOT%prefix/bin/
install -m 644 Src/wmCalendar.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO ogo2ical


%changelog
* Sun Jan 01 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-2
- updated distro definitions.

* Tue Jul 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-1
- new version.

* Fri Jun 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-2
- added buildrequire for libical.

* Thu May 24 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-1
- Initial build.
