%define prefix /usr/X11R6
%define name aswvdial
%define version 1.7
%define release 1

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
Requires: libxml

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
install -s -m 755 aswvdial/netdown $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 aswvdial/netup $RPM_BUILD_ROOT%prefix/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc COPYING ChangeLog INSTALL README XPM.readme


%changelog
* Fri Mar 04 2005 J. Krebs <jkrebs@tconl.com> - 1.7-1
- Initial build.



