%define prefix /usr/X11R6
%define name wmbiff
%define version 0.4.26
%define release 1

Summary: A dockable/swallowed mail notifier
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmbiff.sf.net
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
* Sun Mar  6 2005 Sean Dague <sean@dague.net> 0.4.26-1
- first rpm version




