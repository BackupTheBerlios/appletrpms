%define name wmtimer
%define version 2.92
%define release 5%{?dist}

Summary: wmtimer is a dockable alarm clock
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.darkops.net/wmtimer/
Source0: http://www.darkops.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
WMTimer is a dockable alarm clock for WindowMaker which can be
run in alarm, countdown timer, or chronograph mode. In alarm or
timer mode, you can either execute a command or sound the system
bell when the time is reached. Wmtimer is configurable through
the command line or the GTK GUI.

%prep
%setup -q

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
%{_bindir}/*
%doc COPYING CREDITS Changelog INSTALL README


%changelog
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



