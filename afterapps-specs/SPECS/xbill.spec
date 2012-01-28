%define version 2.1
%define release 1%{?dist}
%define name	xbill

Summary:	Stop Bill from loading his OS into all the computers
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Amusements/Games
Source0:	http://www.xbill.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-Makefile.in.patch
Patch1:		%{name}-%{version}.patch
URL:		http://www.xbill.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glib
Requires:	glibc
Requires:	gtk+
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXi
Requires:	libXmu
Requires:	libXpm
Requires:	libXt
Requires:	Xaw3d
BuildRequires:	gcc-c++
BuildRequires:	glib-devel
BuildRequires:	glibc-devel
BuildRequires:	gtk+-devel
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXmu-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXt-devel
BuildRequires:	Xaw3d-devel

%description
Stop Bill from loading his OS into all the computers.
The xbill game tests your reflexes as you seek out and destroy all
forms of Bill, establish a new operating system throughout the
universe, and boldly go where no geek has gone before. Xbill has
become an increasingly attractive option as the Linux Age progresses,
and it is very popular at Red Hat.

%prep
%setup -q
%patch0
%patch1

%build
./configure --prefix=%{_prefix}         \
	--bindir=%{_bindir}         \
	--mandir=%{_mandir}             \
	--datadir=%{_datadir}      \
	--localstatedir=/var/games

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{_bindir}/xbill
%{_mandir}/man6/xbill.*
%{_datadir}/xbill/bitmaps/apple.xbm
%{_datadir}/xbill/bitmaps/bsd.xbm
%{_datadir}/xbill/bitmaps/bucket.xbm
%{_datadir}/xbill/bitmaps/hand_down.xbm
%{_datadir}/xbill/bitmaps/hand_down_mask.xbm
%{_datadir}/xbill/bitmaps/hand_up.xbm
%{_datadir}/xbill/bitmaps/hand_up_mask.xbm
%{_datadir}/xbill/bitmaps/hurd.xbm
%{_datadir}/xbill/bitmaps/linux.xbm
%{_datadir}/xbill/bitmaps/next.xbm
%{_datadir}/xbill/bitmaps/os2.xbm
%{_datadir}/xbill/bitmaps/palm.xbm
%{_datadir}/xbill/bitmaps/redhat.xbm
%{_datadir}/xbill/bitmaps/sgi.xbm
%{_datadir}/xbill/bitmaps/sun.xbm
%{_datadir}/xbill/pixmaps/about.xpm
%{_datadir}/xbill/pixmaps/apple.xpm
%{_datadir}/xbill/pixmaps/billA_0.xpm
%{_datadir}/xbill/pixmaps/billA_1.xpm
%{_datadir}/xbill/pixmaps/billA_10.xpm
%{_datadir}/xbill/pixmaps/billA_11.xpm
%{_datadir}/xbill/pixmaps/billA_12.xpm
%{_datadir}/xbill/pixmaps/billA_2.xpm
%{_datadir}/xbill/pixmaps/billA_3.xpm
%{_datadir}/xbill/pixmaps/billA_4.xpm
%{_datadir}/xbill/pixmaps/billA_5.xpm
%{_datadir}/xbill/pixmaps/billA_6.xpm
%{_datadir}/xbill/pixmaps/billA_7.xpm
%{_datadir}/xbill/pixmaps/billA_8.xpm
%{_datadir}/xbill/pixmaps/billA_9.xpm
%{_datadir}/xbill/pixmaps/billD_0.xpm
%{_datadir}/xbill/pixmaps/billD_1.xpm
%{_datadir}/xbill/pixmaps/billD_2.xpm
%{_datadir}/xbill/pixmaps/billD_3.xpm
%{_datadir}/xbill/pixmaps/billD_4.xpm
%{_datadir}/xbill/pixmaps/billL_0.xpm
%{_datadir}/xbill/pixmaps/billL_1.xpm
%{_datadir}/xbill/pixmaps/billL_2.xpm
%{_datadir}/xbill/pixmaps/billR_0.xpm
%{_datadir}/xbill/pixmaps/billR_1.xpm
%{_datadir}/xbill/pixmaps/billR_2.xpm
%{_datadir}/xbill/pixmaps/bsd.xpm
%{_datadir}/xbill/pixmaps/bsdcpu.xpm
%{_datadir}/xbill/pixmaps/bucket.xpm
%{_datadir}/xbill/pixmaps/hurd.xpm
%{_datadir}/xbill/pixmaps/icon.xpm
%{_datadir}/xbill/pixmaps/linux.xpm
%{_datadir}/xbill/pixmaps/logo.xpm
%{_datadir}/xbill/pixmaps/maccpu.xpm
%{_datadir}/xbill/pixmaps/next.xpm
%{_datadir}/xbill/pixmaps/nextcpu.xpm
%{_datadir}/xbill/pixmaps/os2.xpm
%{_datadir}/xbill/pixmaps/os2cpu.xpm
%{_datadir}/xbill/pixmaps/palm.xpm
%{_datadir}/xbill/pixmaps/palmcpu.xpm
%{_datadir}/xbill/pixmaps/redhat.xpm
%{_datadir}/xbill/pixmaps/sgi.xpm
%{_datadir}/xbill/pixmaps/sgicpu.xpm
%{_datadir}/xbill/pixmaps/spark_0.xpm
%{_datadir}/xbill/pixmaps/spark_1.xpm
%{_datadir}/xbill/pixmaps/sun.xpm
%{_datadir}/xbill/pixmaps/suncpu.xpm
%{_datadir}/xbill/pixmaps/toaster.xpm
%{_datadir}/xbill/pixmaps/wingdows.xpm
/var/games/xbill.scores.default

%changelog
* Sun Nov 27 2011 J. Krebs <rpm_speedy@yahoo.com> 2.1-1
- initial build.
