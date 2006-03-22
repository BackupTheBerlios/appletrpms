%define prefix /usr
%define name wmradio
%define version 0.9
%define release 2

Summary: wmradio is FM radio card applet for WindowMaker
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://gogo.aquasoft.cz/~cermak/wmradio/
Source0: %{name}-%{version}.tgz
Source1: %{name}-rpm-README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmradio is FM radio card applet for WindowMaker 

%prep
%setup -q

%build
cp %{SOURCE1} .
./configure --prefix=%prefix --disable-libxosd --disable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT

make install

make install-skins

mv $RPM_BUILD_ROOT/share/ $RPM_BUILD_ROOT%prefix/share/

%clean
rm -rf $RPM_BUILD_ROOT

%postun
%prefix/lib/wmradio/*

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%prefix/lib/wmradio/*
%doc README wmradio-rpm-README
%prefix/share/applications/*.desktop
%prefix/share/pixmaps/*.png

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.9-2
- changed prefix path to /usr.

* Mon May 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.9-1
- Initial build.



