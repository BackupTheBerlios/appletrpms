%define prefix /usr/X11R6
%define name wmclockmon
%define version 0.8.0
%define release 1

Summary: digital clock with 7 different styles in either LCD or LED style
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tnemeth.free.fr/projets/dockapps.html
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmclockmon is a nice digital clock with 7 different styles in either
LCD or LED style; uses locales to display weekday and month names.
It also features the internet time.
Includes wmclockmon-cal, a calendar display and wmclockmon-config,
a configuration tool for the package.
Sample .wmclockmonrc files are included in with the doc files. 

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin/
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1/
mkdir -p $RPM_BUILD_ROOT/usr/share/wmclockmon/styles/

install -s -m 755 src/wmclockmon $RPM_BUILD_ROOT%prefix/bin/
install -s -m 755 wmclockmon-config/wmclockmon-config $RPM_BUILD_ROOT%prefix/bin/
install -s -m 755 wmclockmon-cal/wmclockmon-cal $RPM_BUILD_ROOT%prefix/bin/
install -m 644 doc/*.1 $RPM_BUILD_ROOT%prefix/man/man1/
install -m 644 styles/* $RPM_BUILD_ROOT/usr/share/wmclockmon/styles/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
/usr/share/wmclockmon/styles/*
%doc doc/sample*.wmclockmonrc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.8.0-1
- Initial build.

