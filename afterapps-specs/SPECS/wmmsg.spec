%define		name wmmsg
%define		version 1.0.1
%define		release 6%{?dist}

Summary:	dockapp that notifies of incoming messages and events
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://swapspace.net/~matt/wmmsg/
Source0:	http://swapspace.net/~matt/wmmsg/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-alt-desktop.patch
Patch1:		%{name}-%{version}-use_gtk2.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	freetype
Requires:	glib
Requires:	glibc
Requires:	gtk+
Requires:	imlib2
Requires:	libX11
Requires:	libXext
Requires:	libXi
Requires:	libXpm
Requires:	perl
BuildRequires:	freetype-devel
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib2-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXpm-devel

%description
wmmsg is a dockapp that informs you of new events, such as
incoming chat messages, by displaying related icons and arrival
times. A notification program, wmmsg_notify, is included to send
events to the dockapp. This can be called from messaging clients,
or any other useful location. Works with Gaim, X-Chat, etc.

%prep
%setup -q
%patch0
%patch1

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README plugins/* wmmsgrc
%{_bindir}/wmmsg
%{_bindir}/wmmsg_notify
%{_mandir}/man1/wmmsg.1.gz
%{_mandir}/man1/wmmsg_notify.1.gz

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-6
- added altdesktop and gtk2 patches from gentoo.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-5
- added build require for c++ (gcc-c++).

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-2
- changed prefix path to /usr.

* Sat Mar 12 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-1
- Initial build.
