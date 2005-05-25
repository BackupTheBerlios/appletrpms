%define prefix /usr/X11R6
%define name wmcalendar
%define version 0.4.4
%define release 1

Summary: wmCalendar is a calendar dockapp.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sourceforge.net/projects/wmcalendar/
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}.wharf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libical

%description
Staying with v0.4.4 rather than v0.5.0; v0.5.0 has a right-click
crash bug!

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

%prep
%setup -q
%patch0

%build
cd Src
make

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
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO


%changelog
* Thu May 24 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-1
- Initial build.



