%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name asmail
%define version 1.9
%define release 1

Summary: Afterstep Mail Applet
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tigr.net/afterstep/view.php?applet=asmail/data
Source0: http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
Packager: Sean Dague <sean@dague.net>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The application is an AfterStep look & feel multiple e-mail
mailboxes monitor for computers running X Windows.

This application reads the configuration file and launches
as many threads as there are mailboxes defined. There is
no limit on the number of mailboxes to watch. Each mailbox
is verified according to the timeout specified in the
configuration file. The progress and the status of mailboxes
are presented on the screen.

The application may present a summary of all mailboxes or
each mailbox separately (as many as will fit into the picture).
You can specify the XPM picture to use as the backdrop
animation for the status update.


%prep
%setup -q

%build
./configure --prefix=%{__prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    AFTER_RCMAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man5 \
    AFTER_DOC_DIR=$RPM_BUILD_ROOT%{_datadir}/afterstep/doc \
    AFTER_SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/asmail \
    AFTER_PIXDIR=$RPM_BUILD_ROOT%{_datadir}/asmail/pixmaps \
    AFTER_SOUNDDIR=$RPM_BUILD_ROOT%{_datadir}/asmail/sounds \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_datadir}/asmail
%{_datadir}/asmail
%doc CHANGES INSTALL LICENSE README TODO


%changelog
* Fri Nov 24 2006 J. Krebs <rpm_speedy@yahoo.com> 1.9-1
- update to 1.9

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> 1.8-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> 1.8-2
- changed prefix path to /usr.

* Thu Oct 20 2005 J. Krebs <rpm_speedy@yahoo.com> 1.8-1
- update to 1.8

* Sat Feb 26 2005 Sean Dague <sean@dague.net> 1.7-1
- update to 1.7

* Thu Nov 13 2003 Sean Dague <sean@dague.net> 1.6-1
- Intial build
