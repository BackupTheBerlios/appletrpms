%define prefix /usr/X11R6
%define name wmtimer
%define version 2.92
%define release 1

Summary: wmtimer is a dockable alarm clock
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.yuv.info/wmnd/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMTimer is a dockable alarm clock for WindowMaker which can be
run in alarm, countdown timer, or chronograph mode. In alarm or
timer mode, you can either execute a command or sound the system
bell when the time is reached. Wmtimer is configurable through
the command line or the GTK GUI.

%prep
%setup -q

%build
#./configure --prefix=%prefix
cd wmtimer
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 wmtimer/wmtimer $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc COPYING CREDITS Changelog INSTALL README


%changelog
* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.92-1
- Initial build.



