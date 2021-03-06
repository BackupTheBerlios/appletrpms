%define name asapm
%define version 3.1
%define release 4%{?dist}

Summary: Power Management (ACPI / APM) monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tigr.net/afterstep/view.php?applet=asapm/data
Source0: http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libjpeg-devel

%description
asapm is a swallowable applet that monitors the ACPI / APM status
on laptops (battery/AC status, time left). It can execute commands
on a variety of PM events..

Basically, the tool shows you the following:
- The bar-like indicator of the charge left in the battery
  which appears on the left side and is battery-shaped.
  The bottom part shows the charge left in the battery.
  The colors may be customized.
- The top line works as a pair of indicators. You see there
  a battery outline which is "green" when the battery status
  is high, "yellow" when the battery status is low, and
  "red" when the battery status is critical. The colors may
  be customized. The definition of the high, low, critical
  status may be mine :-) or APM daemon's - you can choose.
  The AC plug outline is black while you run the computer
  on the battery and it turns "green" when your computer
  is connected to the mains.
- The second line is the charge left in the battery in percent.
  If the APM daemon does not return a good value for it, the
  display is disabled.
- The third line is the estimate of the time left before the
  complete discharge of the battery. This estimate is either
  provided by the APM daemon or is calculated by this tool
  itself. When there is no estimate available the display is
  disabled.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc CHANGES COPYING INSTALL LICENSE NOTES README TODO asapmrc


%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 3.1-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.1-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.1-2
- changed prefix path to /usr.

* Wed Jul 27 2005 J. Krebs <rpm_speedy@yahoo.com> - 3.1-1
- update to new version

* Tue May 31 2005 J. Krebs <rpm_speedy@yahoo.com> - 3.0-1
- update to new version

* Sat Aug 30 2003 Sean Dague <sean@dague.net> - 2.13-2
- added doc files

* Fri Aug 22 2003 Sean Dague <sean@dague.net> - 2.13-1
- Initial build.


