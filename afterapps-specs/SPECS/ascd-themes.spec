%define prefix /usr
%define name ascd-themes
%define version 1.0
%define release 4

Summary: Themes for ascd, the AfterStep CD player.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://worldserver.oleane.com/rsn/ascd-en.html
Source0: ascd-0.13pr6-themes.tgz
Source1: dwing.tgz
Source2: lcd.tar.gz
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
mkdir -p $RPM_BUILD_ROOT%prefix/share/ascd/Themes/

cp themes.tar $RPM_BUILD_ROOT%prefix/share/ascd/Themes/
cp %{SOURCE1} $RPM_BUILD_ROOT%prefix/share/ascd/Themes/
cp %{SOURCE2} $RPM_BUILD_ROOT%prefix/share/ascd/Themes/

cd $RPM_BUILD_ROOT%prefix/share/ascd/Themes/

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
%prefix/share/ascd/Themes/*/*


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0-4
- changed prefix path to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-3
- Changed Themes path to /usr/X11R6/share/ascd/Themes.

* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-2
- Revamped the tarball setup.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build.
