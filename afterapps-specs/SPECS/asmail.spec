%define prefix /usr/X11R6
%define name asmail
%define version 1.6 
%define release 1

Summary: Afterstep Mail Applet
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
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
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%prefix/bin \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%prefix/man/man1 \
    AFTER_RCMAN_DIR=$RPM_BUILD_ROOT%prefix/man/man5 \
    AFTER_DOC_DIR=$RPM_BUILD_ROOT%prefix/share/afterstep/doc \
    AFTER_SHAREDIR=$RPM_BUILD_ROOT%prefix/share/asmail \
    AFTER_PIXDIR=$RPM_BUILD_ROOT%prefix/share/asmail/pixmaps \
    AFTER_SOUNDDIR=$RPM_BUILD_ROOT%prefix/share/asmail/sounds \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%prefix/man/man5/*
%prefix/share/asmail
%doc CHANGES INSTALL LICENSE README TODO


%changelog
* Thu Nov 13 2003 Sean Dague <sean@dague.net> 1.6 -1
- Intial build


