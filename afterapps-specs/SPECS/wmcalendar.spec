%define prefix /usr/X11R6
%define name wmcalendar
%define version 0.5.0
%define release 1

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

egrep 'Fedora Core release 4' /etc/fedora-release && make CC=gcc32
egrep 'Fedora Core release 4' /etc/fedora-release || make

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
* Tue Jul 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-1
- new version.

* Fri Jun 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-2
- added buildrequire for libical.

* Thu May 24 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-1
- Initial build.
