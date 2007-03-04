%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name ascd
%define version 0.13.2
%define release 7

Summary: Audio CD player
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://worldserver.oleane.com/rsn/ascd-en.html
Source0: http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
Source1: http://worldserver.oleane.com/rsn/Archives/ascd-0.13pr6-themes.tgz
Source2: http://worldserver.oleane.com/rsn/Archives/dwing.tgz
Source3: http://worldserver.oleane.com/rsn/Archives/lcd.tar.gz
Patch0: ascd-0.13.2.a.patch
Patch1: ascd-0.13.2.b.patch
Patch2: ascd-0.13.2.c.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: ascd-themes
Provides: ascd-themes

%description
A swallowable applet allows to control the CD-ROM and provides
the familiar controls like a regular CD player. In effect, this
is an advanced CD player with a fully customizable interface and
support for themes.

%prep
%setup -q -n ascd-%{version} -a 1 -a 2 -a 3

%patch0 -p1 -b .a
%patch1 -p1 -b .b
%patch2 -p1 -b .c

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 ascd/ascd $RPM_BUILD_ROOT%{_bindir}/
install -m 644 ascd/ascd.man $RPM_BUILD_ROOT%{_mandir}/man1/ascd.1

cd $RPM_BUILD_DIR/ascd-%{version}/ascd/themes/
gunzip themes-manual.ps.gz
tar xvf default.tar
tar xvf themes.tar

cd $RPM_BUILD_DIR/ascd-%{version}/ascd-0.13pr6-themes/
tar xvf themes.tar -C $RPM_BUILD_DIR/ascd-%{version}/ascd/themes/Themes/

mv $RPM_BUILD_DIR/ascd-%{version}/dwing/ $RPM_BUILD_DIR/ascd-%{version}/ascd/themes/Themes/
mv $RPM_BUILD_DIR/ascd-%{version}/lcd/ $RPM_BUILD_DIR/ascd-%{version}/ascd/themes/Themes/

install -d $RPM_BUILD_ROOT%{_datadir}/ascd/Default/
install -d $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

cp -ar $RPM_BUILD_DIR/ascd-%{version}/ascd/themes/Default/* $RPM_BUILD_ROOT%{_datadir}/ascd/Default/
cp -ar $RPM_BUILD_DIR/ascd-%{version}/ascd/themes/Themes/* $RPM_BUILD_ROOT%{_datadir}/ascd/Themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/ascd/
%doc README ascd/doc/* ascd/themes/themes-manual.ps

%changelog
* Sat Mar 03 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-7
- merged ascd and ascd-themes; ascd-themes obsolete.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-6
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-5
- changed prefix path to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-4
- Changed Themes dir to /usr/X11R6/share/ascd/Themes.

* Sat Feb 27 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-3
- Changed tarball to that provided by tigr.net/afterstep/.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-2
- Changed themes from /usr/local/share to /usr/share.

* Mon Feb 07 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.13.2-1
- Initial build.
