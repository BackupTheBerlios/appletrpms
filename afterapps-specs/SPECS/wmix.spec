%define prefix /usr
%define name wmix
%define version 3.2
%define release 2

Summary: dockapp mixer utilizing the OSS mixer API
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.dockapps.com/file.php/id/58
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
- This is a complete dockapp mixer utilizing the OSS mixer API
- Has a nice On-Screen-Display to visualize current volume levels
- Can adjust main volume, balance, recording status, and
  mute/unmute channels
- Supports mousewheel to adjust the volume settings
- Supports user specified signals to adjust the volume remotely
- User configuration file can be used to set options

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1

install -s -m 755 wmix $RPM_BUILD_ROOT%prefix/bin
install -m 644 wmix.1x.gz $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS BUGS COPYING INSTALL NEWS README sample.wmixrc


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 3.2-2
- changed prefix path to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 3.2-1
- Initial build.



