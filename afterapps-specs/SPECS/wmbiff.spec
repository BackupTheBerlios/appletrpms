%define prefix /usr
%define name wmbiff
%define version 0.4.27
%define release 2

Summary: A dockable/swallowed mail notifier
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmbiff.sf.net
Source0: %{name}-%{version}.tar.gz
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
./configure --prefix=%prefix
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man*/*
%dir %prefix/share/%{name}
%prefix/share/%{name}/*
%dir %prefix/lib/%{name}
%prefix/lib/%{name}/*

%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README* TODO

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> 0.4.27-2
- changed prefix path to /usr.
* Wed Nov 09 2005 J. Krebs <rpm_speedy@yahoo.com> 0.4.27-1
- new version.
* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> 0.4.26-2
- added require for ruby.
* Sun Mar  6 2005 Sean Dague <sean@dague.net> 0.4.26-1
- first rpm version




