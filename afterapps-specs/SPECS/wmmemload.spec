%define prefix /usr/X11R6
%define name wmmemload
%define version 0.1.6
%define release 1

Summary: memory monitor dockapp which displays free memory and swap space
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.markstaggs.net/cgi-bin/index.pl?&page=wmmemload
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmmemload is a simple dockapp for WindowMaker on X Windows that
displays memory and swap space usage. It is very heavily based
on WMMemMon and WMCPULoad by Seiichi SATO. 

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 src/wmmemload $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS


%changelog
* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.1.6-1
- Initial build.



