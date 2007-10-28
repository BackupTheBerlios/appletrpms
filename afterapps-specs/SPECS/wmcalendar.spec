%define lictest	%(rpm -q --queryformat='%{VERSION}' libical)
%define licver	%lictest 
%define name wmcalendar
%define version 0.5.2
%define release 4%{?dist}

Summary: wmCalendar is a calendar dockapp
Name: %name
Version: %version
Release: %release
License: GPLv2+
Group: AfterStep/Applets
URL: http://sourceforge.net/projects/wmcalendar/
Source0: http://easynews.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.ogo2ical
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libical >= %{licver}
Buildrequires: libical-devel

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

cp %{SOURCE1} ogo2ical

%build
cd Src

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 Src/wmCalendar $RPM_BUILD_ROOT%{_bindir}/
install -m 644 Src/wmCalendar.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO ogo2ical


%changelog
* Fri Oct 12 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-4
- added test for libical version, updated for libical 0.27.

* Fri Jun 15 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-3
- spec file cleanup.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-2
- added distro info to release.

* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-1
- New version.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-5
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-4
- changed prefix path to /usr.

* Tue Jan 10 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-3
- added gcc4 patch (thank you gentoo team, Michele Noberasco).

* Sun Jan 01 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-2
- updated distro definitions.

* Tue Jul 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-1
- new version.

* Fri Jun 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-2
- added buildrequire for libical.

* Thu May 24 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.4-1
- Initial build.
