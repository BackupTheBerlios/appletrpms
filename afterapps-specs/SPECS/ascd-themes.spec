%define name ascd-themes
%define version 1.0
%define release 2

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
/usr/share/ascd/Themes.

%prep
%setup -q -n ascd-0.13pr6-themes

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/ascd/Themes/

cp themes.tar $RPM_BUILD_ROOT/usr/share/ascd/Themes/
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/share/ascd/Themes/
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/share/ascd/Themes/

cd $RPM_BUILD_ROOT/usr/share/ascd/Themes/

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
/usr/share/ascd/Themes/*/*


%changelog
* Tue Feb 22 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-2
- Revamped the tarball setup.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0-1
- Initial build.




