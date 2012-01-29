%define		name wmbiff
%define		version 0.4.27
%define		release 6%{?dist}

Summary:	A dockable/swallowed mail notifier
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://wmbiff.sf.net
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	gnutls  
Requires:	libgcrypt
Requires:	libgpg-error  
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	zlib  
BuildRequires:	glibc-devel
BuildRequires:	gnutls-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	zlib-devel

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
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir} 
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING FAQ NEWS README* TODO
%{_bindir}/%{name}
%{_libdir}/%{name}/security.debian.rb
%{_mandir}/man1/wmbiff.1.gz
%{_mandir}/man5/wmbiffrc.5.gz
%{_datadir}/%{name}/skins/wmbiff-master-contrast.xpm
%{_datadir}/%{name}/skins/wmbiff-master-led.xpm

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.4.27-6
- updated sourceforge URLs

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.4.27-5
- added libdir to configure for build under x86_64.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.27-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.27-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.27-2
- changed prefix path to /usr.

* Wed Nov 09 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.27-1
- new version.

* Mon Apr 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.26-2
- added require for ruby.

* Sun Mar  6 2005 Sean Dague <sean@dague.net> - 0.4.26-1
- first rpm version




