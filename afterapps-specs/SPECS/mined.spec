%define name	mined
%define version	2012.20
%define release	1%{?dist}

Summary:	a powerful text editor with extensive Unicode and CJK support
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Applications/Editors
URL:		http://towo.net/mined/
Source0:	http://towo.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	ncurses
Buildrequires:	glibc-devel
Buildrequires:	ncurses-devel

%description
mined is a powerful text editor with extensive Unicode and CJK support.

%prep
%setup -q

%build
make -C src -f makefile.linux PREFIX=%{_prefix} LIBDIR=%{_libdir} GLDOPTS=" -ltinfo "

%install
rm -rf $RPM_BUILD_ROOT

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/mined
%{_bindir}/minmacs
%{_bindir}/mpico
%{_bindir}/mstar
%{_bindir}/umined
%{_bindir}/uterm
%{_bindir}/xmined
%{_datadir}/applications/mined.desktop
%{_datadir}/mined/bin/mterm
%{_datadir}/mined/bin/umined
%{_datadir}/mined/bin/uprint
%{_datadir}/mined/bin/uterm
%{_datadir}/mined/bin/wined
%{_datadir}/mined/bin/wined.bat
%{_datadir}/mined/bin/xmined
%{_datadir}/mined/conf_user/konsole/xterm-modified.keytab
%{_datadir}/mined/conf_user/kp5
%{_datadir}/mined/conf_user/MINED-VMS.COM
%{_datadir}/mined/conf_user/mlterm/key
%{_datadir}/mined/conf_user/mlterm/main
%{_datadir}/mined/conf_user/profile.mined
%{_datadir}/mined/conf_user/terminator/options
%{_datadir}/mined/conf_user/Xdefaults.mined
%{_datadir}/mined/conf_user/xinitrc.mined
%{_datadir}/mined/doc_user/cancel.html
%{_datadir}/mined/doc_user/changes.html
%{_datadir}/mined/doc_user/combined.png
%{_datadir}/mined/doc_user/combining.png
%{_datadir}/mined/doc_user/contact.html
%{_datadir}/mined/doc_user/design.html
%{_datadir}/mined/doc_user/dollar.gif
%{_datadir}/mined/doc_user/donate.html
%{_datadir}/mined/doc_user/download.html
%{_datadir}/mined/doc_user/euro1.gif
%{_datadir}/mined/doc_user/features.html
%{_datadir}/mined/doc_user/file-chooser.png
%{_datadir}/mined/doc_user/handr.gif
%{_datadir}/mined/doc_user/haninfo-big5.png
%{_datadir}/mined/doc_user/haninfo-menu.png
%{_datadir}/mined/doc_user/haninfo-utf8.png
%{_datadir}/mined/doc_user/header.html
%{_datadir}/mined/doc_user/index-dl.html
%{_datadir}/mined/doc_user/index.html
%{_datadir}/mined/doc_user/keyboard.html
%{_datadir}/mined/doc_user/logo.gif
%{_datadir}/mined/doc_user/menu.png
%{_datadir}/mined/doc_user/minedfav.ico
%{_datadir}/mined/doc_user/mined.html
%{_datadir}/mined/doc_user/mined-html.png
%{_datadir}/mined/doc_user/mined-mintty.png
%{_datadir}/mined/doc_user/mined-pw.png
%{_datadir}/mined/doc_user/minedscr.ico
%{_datadir}/mined/doc_user/mined-sep.png
%{_datadir}/mined/doc_user/mined-small-10x20.png
%{_datadir}/mined/doc_user/mined-small-haninfo.png
%{_datadir}/mined/doc_user/mined-small-html.png
%{_datadir}/mined/doc_user/mined-small-picklist.png
%{_datadir}/mined/doc_user/mined-small-pw.png
%{_datadir}/mined/doc_user/mined-small-sep.png
%{_datadir}/mined/doc_user/mined-small-uni.png
%{_datadir}/mined/doc_user/mined-uni.png
%{_datadir}/mined/doc_user/mnemodoc.html
%{_datadir}/mined/doc_user/navigate.html
%{_datadir}/mined/doc_user/new.gif
%{_datadir}/mined/doc_user/new-rot.gif
%{_datadir}/mined/doc_user/overview.html
%{_datadir}/mined/doc_user/paypal_donate.gif
%{_datadir}/mined/doc_user/paypal_logo.gif
%{_datadir}/mined/doc_user/paypal_payments.gif
%{_datadir}/mined/doc_user/picklist.png
%{_datadir}/mined/doc_user/rectangular.png
%{_datadir}/mined/doc_user/screenshots.html
%{_datadir}/mined/doc_user/script-arabic.gif
%{_datadir}/mined/doc_user/script-cyrillic.gif
%{_datadir}/mined/doc_user/script-greek.gif
%{_datadir}/mined/doc_user/script-han.gif
%{_datadir}/mined/doc_user/script-hebrew.gif
%{_datadir}/mined/doc_user/script-highlighting.png
%{_datadir}/mined/doc_user/script-hiragana.gif
%{_datadir}/mined/doc_user/script-thai.gif
%{_datadir}/mined/doc_user/separated.png
%{_datadir}/mined/doc_user/soft82_award_130x130.gif
%{_datadir}/mined/doc_user/softpedia_free_award_f.gif
%{_datadir}/mined/doc_user/term-big5-cxterm.png
%{_datadir}/mined/doc_user/term-cygwin.png
%{_datadir}/mined/doc_user/term-dos.png
%{_datadir}/mined/doc_user/terminal.png
%{_datadir}/mined/doc_user/term-mintty.png
%{_datadir}/mined/doc_user/thankyou.html
%{_datadir}/mined/doc_user/unicode.html
%{_datadir}/mined/doc_user/unicode.org.png
%{_datadir}/mined/doc_user/uterm.html
%{_datadir}/mined/help/mined.hlp
%{_datadir}/mined/package_doc/CHANGES
%{_datadir}/mined/package_doc/LICENCE.GPL
%{_datadir}/mined/package_doc/README
%{_datadir}/mined/package_doc/VERSION
%{_datadir}/mined/setup_install/bin/bdf18to20
%{_datadir}/mined/setup_install/bin/configure-xterm
%{_datadir}/mined/setup_install/bin/installfonts
%{_datadir}/mined/setup_install/bin/makeprint
%{_datadir}/mined/setup_install/bin/mkicon
%{_datadir}/mined/setup_install/bin/postinstall
%{_datadir}/mined/setup_install/bin/preremove
%{_datadir}/mined/setup_install/bin/setupreg.sh
%{_datadir}/mined/setup_install/mined.desktop
%{_datadir}/mined/setup_install/mined.ico
%{_datadir}/mined/setup_install/mined.png
%{_datadir}/mined/setup_install/mined.xpm
%{_datadir}/mined/setup_install/win/deleteall.bat
%{_datadir}/mined/setup_install/win/install.sh
%{_datadir}/mined/setup_install/win/MinEd-AD.lnk
%{_datadir}/mined/setup_install/win/MinEd-PF.lnk
%{_datadir}/mined/setup_install/win/MinEd*Web*Manual.url
%{_datadir}/mined/setup_install/win/Uninst-AD.lnk
%{_datadir}/mined/setup_install/win/uninstall.sh
%{_datadir}/mined/setup_install/win/Uninst-PF.lnk
%{_datadir}/pixmaps/mined.xpm
%{_mandir}/man1/mined.1.*
%{_mandir}/man1/minmacs.1.*
%{_mandir}/man1/mpico.1.*
%{_mandir}/man1/mstar.1.*
%{_mandir}/man1/umined.1.*
%{_mandir}/man1/uterm.1.*
%{_mandir}/man1/xmined.1.*

%doc CHANGES DESCR LICENCE.GPL PACKAGE.DOC README.creole VERSION

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 2012.20-1
- new version.

* Fri Jul 16 2011 J. Krebs <rpm_speedy@yahoo.com> - 2011.17-1
- new version.

* Mon Feb 01 2011 J. Krebs <rpm_speedy@yahoo.com> - 2000.16-2
- Added link for libtinfo.

* Mon Mar 01 2010 J. Krebs <rpm_speedy@yahoo.com> - 2000.16-1
- New version.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 2000.15.4-1
- New version.

* Sat Aug 09 2008 J. Krebs <rpm_speedy@yahoo.com> - 2000.14-2
- Added termio patch (from Suse) for build under AMD84.

* Tue Aug 21 2007 J. Krebs <rpm_speedy@yahoo.com> - 2000.14-1
- Initial build.
