%define prefix /usr/X11R6
%define name wmnd
%define version 0.4.11
%define release 1

Summary: wmnd is a network monitoring dockapp.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.yuv.info/wmnd/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMND (WindowMaker Network Devices) is a network monitoring
dockapp for Window Maker (and compatibles) for many operative systems.
Improved and based on WMiFS 1.3b, the version 0.2 of WMND is almost
totally written by Timecop, given the optimization and flexibility and
now consumes less cpu than wmmon. Version >= 0.3 WMND is now
maintained by wave++, which added new display modes and several new
drivers. Enjoy!

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
install -s -m 755 src/wmnd $RPM_BUILD_ROOT%prefix/bin/
install -m 644 doc/wmnd.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO examples/wmndrc


%changelog
* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.11-1
- Initial build.



