%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name ascd-themes
%define version 1.0
%define release 5

Summary: Themes for ascd, the AfterStep CD player.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://worldserver.oleane.com/rsn/ascd-en.html
Source0: http://worldserver.oleane.com/rsn/Archives/ascd-0.13pr6-themes.tgz
Source1: http://worldserver.oleane.com/rsn/Archives/dwing.tgz
Source2: http://worldserver.oleane.com/rsn/Archives/lcd.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: ascd

%description
Themes for ascd, the AfterStep CD player.  Includes ten from
Denis Bourez and one from Michele Campeotto.  These install to
%prefix/share/ascd/Themes.

%prep
%setup -q -n ascd-0.13pr6-themes

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

cp themes.tar $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

cd $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

tar xvf themes.tar
tar xvzf dwing.tgz
tar xvzf lcd.tar.gz

rm -f themes.tar
rm -f dwing.tgz
rm -f lcd.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/ascd
%dir %{_datadir}/ascd/Themes
%dir %{_datadir}/ascd/Themes/*
%{_datadir}/ascd/Themes/*/*

%changelog
* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0-4
- changed prefix path to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-3
- Changed Themes path to /usr/X11R6/share/ascd/Themes.

* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-2
- Revamped the tarball setup.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build.
