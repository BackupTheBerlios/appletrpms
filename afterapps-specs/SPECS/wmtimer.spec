%define		name wmtimer
%define		version 2.92
%define		release 6%{?dist}

Summary:	a dockable alarm clock
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.darkops.net/wmtimer/
Source0:	http://www.darkops.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-counter-fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	glibc
Requires:	gtk2
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
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	pango-devel

%description
WMTimer is a dockable alarm clock for WindowMaker which can be
run in alarm, countdown timer, or chronograph mode. In alarm or
timer mode, you can either execute a command or sound the system
bell when the time is reached. Wmtimer is configurable through
the command line or the GTK GUI.

%prep
%setup -q
%patch0

%build
cd wmtimer
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 wmtimer/wmtimer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING CREDITS Changelog README
%{_bindir}/wmtimer

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.92-6
- added counter patch from gentoo.

* Thu Aug 06 2009 J. Krebs <rpm_speedy@yahoo.com> - 2.92-5
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.92-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.92-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 2.92-2
- changed prefix path to /usr.

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.92-1
- Initial build.



