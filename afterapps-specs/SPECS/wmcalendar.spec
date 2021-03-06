%define		lictest	%(rpm -q --queryformat='%{VERSION}' libical)
%define		licver	%lictest 
%define		name wmcalendar
%define		version 0.5.2
%define		release 7%{?dist}

Summary:	a calendar dockapp
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://sourceforge.net/projects/wmcalendar/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.ogo2ical
Patch0:		wmcalendar-0.5.2-exit-sin-and-cos.patch
Patch1:		wmcalendar-0.5.2-rename_kill_func.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	glibc
Requires:	gtk2
Requires:	libical >= %{licver}
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
BuildRequires:	gtk2-devel
BuildRequires:	libical-devel
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	pango-devel

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

make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

cd Src

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/wmCalendar
%{_mandir}/man1/wmCalendar.*
%doc BUGS CHANGES COPYING HINTS README TODO ogo2ical

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-7
- updated sourceforge URLs.

* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-6
- updated patch0 (exit-sin-cos) to improve library links.

* Tue Aug 04 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.5.2-5
- added build patches for Fedora 11.

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
