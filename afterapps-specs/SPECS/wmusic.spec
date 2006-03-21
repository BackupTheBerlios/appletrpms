%define prefix /usr
%define name wmusic
%define version 1.5.0
%define release 2

Summary: Windowmaker dockapp that remote controls xmms.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://home.jtan.com/~john/wmusic/
Source0: %{name}-%{version}.tar.gz
Requires:   xmms >= 1.0.0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xmms-devel

%description
wmusic is a dockapp that remote-controls xmms. Here is a list
of the features:

- VCR style controls including fast rewind and fast forward
- Time and Playlist position display
- Super stylee rotating arrow
- Hiding of the xmms windows (on startup and through middle-click)
- AfterStep users, add this line to ~/GNUstep/Library/AfterStep/wharf:
	*Wharf wmusic - Swallow "wmusic" wmusic -w &
- Sawfish users, grab Tiger-T's DockMill theme, and apply it to the running
  dockapp with the -w flag on. See the theme's README for more details.
- KDE users can use the "Dock Application Bar" to dock wmusic, don't forget
  the -w flag to launch wmusic. Right-Click on Kicker, then pick:
  Add->Extension->Dock Application Bar


%prep
%setup -q -n %name-%version

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 src/wmusic $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc COPYING README


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.5.0-1
- Initial build.



