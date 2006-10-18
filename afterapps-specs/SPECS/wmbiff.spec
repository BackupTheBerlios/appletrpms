%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define _libdir %{__prefix}/lib
%define name wmbiff
%define version 0.4.27
%define release 3

Summary: A dockable/swallowed mail notifier
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmbiff.sf.net
Source0: http://internap.dl.sourceforge.net/sourceforge/wmbiff/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: ruby

%description 
%{name} is an WindowMaker docking utility, that displays
number of total messages count or unread mail messages count in
differrent mailboxes.

At this moment unix-style (mbox), maildir, POP3, APOP and IMAP
mailboxes are supported. WMBiff also understands Licq's history files.
WMBiff supports up to 5 mailboxes (but you can start 2 or more
wmbiff's with differrent configs).

%prep
%setup -q

%build
./configure --prefix=%{__prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*

%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README* TODO

%changelog
* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> 0.4.27-3
- Updated Source path.
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> 0.4.27-2
- changed prefix path to /usr.
* Wed Nov 09 2005 J. Krebs <rpm_speedy@yahoo.com> 0.4.27-1
- new version.
* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> 0.4.26-2
- added require for ruby.
* Sun Mar  6 2005 Sean Dague <sean@dague.net> 0.4.26-1
- first rpm version




