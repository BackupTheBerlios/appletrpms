%define prefix /usr/X11R6
%define name ascd
%define version 0.13.2
%define release 3

Summary: Audio CD player
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://worldserver.oleane.com/rsn/ascd-en.html
Source0: %{name}-%{version}.tar.gz
Patch0: ascd-0.13.2.a.patch
Patch1: ascd-0.13.2.b.patch
Patch2: ascd-0.13.2.c.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet allows to control the CD-ROM and provides
the familiar controls like a regular CD player. In effect, this
is an advanced CD player with a fully customizable interface and
support for themes.

%prep
%setup -q -n ascd-%{version}

%patch0 -p1 -b .a
%patch1 -p1 -b .b
%patch2 -p1 -b .c

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/share/ascd/Default/
mkdir -p $RPM_BUILD_ROOT/usr/share/ascd/Themes/default/quick/

install -s -m 755 ascd/ascd $RPM_BUILD_ROOT%prefix/bin/
install -m 644 ascd/ascd.man $RPM_BUILD_ROOT%prefix/man/man1/ascd.1

cd ascd/themes
tar xvf default.tar
tar xvf themes.tar
gunzip themes-manual.ps.gz

install -m 644 Default/* $RPM_BUILD_ROOT/usr/share/ascd/Default/
cd Themes
install -m 644 default/*.xpm $RPM_BUILD_ROOT/usr/share/ascd/Themes/default/
install -m 644 default/Theme $RPM_BUILD_ROOT/usr/share/ascd/Themes/default/

cd default
install -m 644 quick/* $RPM_BUILD_ROOT/usr/share/ascd/Themes/default/quick/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
/usr/share/ascd/Default/*
/usr/share/ascd/Themes/default/*
%doc README ascd/doc/* ascd/themes/themes-manual.ps


%changelog
* Sat Feb 27 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-3
- Changed tarball to that provided by tigr.net/afterstep/.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-2
- Changed themes from /usr/local/share to /usr/share.

* Mon Feb 07 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-1
- Initial build.



