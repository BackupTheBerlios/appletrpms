%define prefix /usr
%define name aswvdial
%define version 1.7
%define release 4

Summary: ASwvdial is a dock/wharf/slit app for wvdial
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.ma-scha.de/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml-devel
Requires: libxml wvdial

%description
ASwvdial is a dock/wharf/slit app for wvdial.

%prep
%setup -q -n aswvdial

%build
#./configure --prefix=%prefix
cd aswvdial
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 aswvdial/aswvdial $RPM_BUILD_ROOT%prefix/bin
install -m 755 aswvdial/netdown $RPM_BUILD_ROOT%prefix/bin
install -m 755 aswvdial/netup $RPM_BUILD_ROOT%prefix/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc COPYING ChangeLog INSTALL README XPM.readme


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.7-4
- changed prefix path to /usr.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-3
- Maker script files install better.

* Sun Jun 12 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-2
- Added require for wvdial (duh).

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-1
- Initial build.



