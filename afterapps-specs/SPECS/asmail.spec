%define		name asmail
%define		version 2.1
%define		release 2%{?dist}

Summary:	Afterstep Mail Applet
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://tigr.net/afterstep/view.php?applet=asmail/data
Source0:	http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libICE libSM libX11 libXext libXpm openssl
BuildRequires:	libICE-devel libSM-devel libX11-devel
BuildRequires:	libXext-devel libXpm-devel openssl-devel

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
./configure --prefix=%{_prefix}

make LIBS_X="-L%{_libdir} -lX11 -lSM -lICE -lXpm -lXext -lcrypto"

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
%doc CHANGES INSTALL LICENSE README TODO
%{_bindir}/asmail
%{_datadir}/%{name}/pixmaps/e-no.xpm
%{_datadir}/%{name}/pixmaps/e0.xpm
%{_datadir}/%{name}/pixmaps/e1.xpm
%{_datadir}/%{name}/pixmaps/e10.xpm
%{_datadir}/%{name}/pixmaps/e11.xpm
%{_datadir}/%{name}/pixmaps/e12.xpm
%{_datadir}/%{name}/pixmaps/e13.xpm
%{_datadir}/%{name}/pixmaps/e14.xpm
%{_datadir}/%{name}/pixmaps/e15.xpm
%{_datadir}/%{name}/pixmaps/e16.xpm
%{_datadir}/%{name}/pixmaps/e17.xpm
%{_datadir}/%{name}/pixmaps/e18.xpm
%{_datadir}/%{name}/pixmaps/e19.xpm
%{_datadir}/%{name}/pixmaps/e2.xpm
%{_datadir}/%{name}/pixmaps/e20.xpm
%{_datadir}/%{name}/pixmaps/e21.xpm
%{_datadir}/%{name}/pixmaps/e22.xpm
%{_datadir}/%{name}/pixmaps/e23.xpm
%{_datadir}/%{name}/pixmaps/e24.xpm
%{_datadir}/%{name}/pixmaps/e25.xpm
%{_datadir}/%{name}/pixmaps/e26.xpm
%{_datadir}/%{name}/pixmaps/e27.xpm
%{_datadir}/%{name}/pixmaps/e28.xpm
%{_datadir}/%{name}/pixmaps/e29.xpm
%{_datadir}/%{name}/pixmaps/e3.xpm
%{_datadir}/%{name}/pixmaps/e30.xpm
%{_datadir}/%{name}/pixmaps/e4.xpm
%{_datadir}/%{name}/pixmaps/e5.xpm
%{_datadir}/%{name}/pixmaps/e6.xpm
%{_datadir}/%{name}/pixmaps/e7.xpm
%{_datadir}/%{name}/pixmaps/e8.xpm
%{_datadir}/%{name}/pixmaps/e9.xpm
%{_datadir}/%{name}/pixmaps/m-e0.xpm
%{_datadir}/%{name}/pixmaps/m-e1.xpm
%{_datadir}/%{name}/pixmaps/m-e10.xpm
%{_datadir}/%{name}/pixmaps/m-e11.xpm
%{_datadir}/%{name}/pixmaps/m-e12.xpm
%{_datadir}/%{name}/pixmaps/m-e13.xpm
%{_datadir}/%{name}/pixmaps/m-e14.xpm
%{_datadir}/%{name}/pixmaps/m-e15.xpm
%{_datadir}/%{name}/pixmaps/m-e16.xpm
%{_datadir}/%{name}/pixmaps/m-e17.xpm
%{_datadir}/%{name}/pixmaps/m-e18.xpm
%{_datadir}/%{name}/pixmaps/m-e19.xpm
%{_datadir}/%{name}/pixmaps/m-e2.xpm
%{_datadir}/%{name}/pixmaps/m-e20.xpm
%{_datadir}/%{name}/pixmaps/m-e21.xpm
%{_datadir}/%{name}/pixmaps/m-e22.xpm
%{_datadir}/%{name}/pixmaps/m-e23.xpm
%{_datadir}/%{name}/pixmaps/m-e24.xpm
%{_datadir}/%{name}/pixmaps/m-e25.xpm
%{_datadir}/%{name}/pixmaps/m-e26.xpm
%{_datadir}/%{name}/pixmaps/m-e27.xpm
%{_datadir}/%{name}/pixmaps/m-e28.xpm
%{_datadir}/%{name}/pixmaps/m-e29.xpm
%{_datadir}/%{name}/pixmaps/m-e3.xpm
%{_datadir}/%{name}/pixmaps/m-e30.xpm
%{_datadir}/%{name}/pixmaps/m-e4.xpm
%{_datadir}/%{name}/pixmaps/m-e5.xpm
%{_datadir}/%{name}/pixmaps/m-e6.xpm
%{_datadir}/%{name}/pixmaps/m-e7.xpm
%{_datadir}/%{name}/pixmaps/m-e8.xpm
%{_datadir}/%{name}/pixmaps/m-e9.xpm
%{_datadir}/%{name}/sounds/clink.au
%{_datadir}/%{name}/sounds/drip.au
%{_mandir}/man1/asmail.*
%{_mandir}/man5/asmailrc.*

%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> 2.1-2
- cleaned up spec file.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> 2.1-1
- new version, added distro info to release.

* Tue Feb 27 2007 J. Krebs <rpm_speedy@yahoo.com> 2.0-1
- new version.

* Fri Feb 23 2007 J. Krebs <rpm_speedy@yahoo.com> 1.9-2
- removed packager line.

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
