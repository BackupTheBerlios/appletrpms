%define		name wmudmount
%define		version 1.8
%define		release 1%{?dist}

Summary:	dockapp to mount filesystems using udisks
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://sourceforge.net/projects/wmudmount/
Source0:	http://www.dockapps.org/download.php/id/836/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-notify.c.patch
Patch1:		%{name}-%{version}-configure.ac.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	dbus-libs
Requires:	dbus-glib
Requires:	glib2
Requires:	glibc
Requires:	gnome-keyring
Requires:	gtk2
Requires:	libgnome-keyring
Requires:	libnotify
Requires:	libX11
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk2-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	libX11-devel
BuildRequires:	ImageMagick

%description
wmudmount is a filesystem mounter that uses udisks to handle notification of
new filesystems and mounting of the filesystems as a non-root user. It also
includes a mode to display the mounted filesystems with the least free space
percentage (similar to wmfsm).

%prep

%setup -q
%patch0
%patch1

%build
./bootstrap

./configure --prefix=%{_prefix} --mandir=%{_mandir}

make LIBS=" -lm -lX11"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/16x16/apps/%{name}-lock.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}-unlock.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}-lock.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}-unlock.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-lock.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-unlock.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-lock.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-unlock.svg

%changelog
* Tue May 24 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.8-1
- new version.

* Mon Dec 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.6-2
- added build require for ImageMagick (convert).

* Sun Aug 29 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.6-1
- initial build.
