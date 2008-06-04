%define aitest	%(rpm -q --queryformat='%{VERSION}' libAfterImage)
%define aiver	%aitest 
%define version 9.02
%define release 2%{?dist}
%define name	rxvt-unicode
%define epoch	2

Summary:	rxvt-unicode is a unicode version of rxvt
Name:		%name
Version:	%version
Release:	%release
Epoch:		%epoch
License:	GPLv2+
Group:		User Interface/X
URL:		http://software.schmorp.de/pkg/rxvt-unicode.html
Source0:	http://dist.schmorp.de/rxvt-unicode/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-stropts.h.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	perl-devel libXpm-devel libXft-devel freetype-devel
BuildRequires:	libAfterImage-devel >= 1.15
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  /usr/bin/tic
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
Requires:	perl libXpm libXft freetype
Requires:	libAfterImage >= %{aiver}

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q
%patch0

%build

./configure --prefix=%{_prefix} --libdir=%{_libdir} \
		--with-xpm-includes=%{_includedir}/X11 \
		--with-xpm-library=%{_libdir} \
		--enable-afterimage

make CFLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=%{name}
Comment=rxvt-unicode is a unicode version of rxvt
Exec=urxvt
Terminal=false
Type=Application" > %{name}.desktop
                                                                                
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category System						  \
  --add-category Utility					  \
  --add-category TerminalEmulator                                 \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING Changes INSTALL README.FAQ README.configure doc/README.xvt doc/etc doc/changes.txt
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_libdir}/urxvt

%changelog
* Mon Jun 02 2008 J. Krebs <rpm_speedy@yahoo.com> - 2:9.02-2
- added patch for stropts.h - Fedora 9 and later don't ship it.

* Fri Feb 02 2008 J. Krebs <rpm_speedy@yahoo.com> - 2:9.02-1
- new version.

* Fri Jan 25 2008 J. Krebs <rpm_speedy@yahoo.com> - 2:9.0-1
- new version.

* Mon Dec 24 2007 J. Krebs <rpm_speedy@yahoo.com> - 2:8.9-1
- new version.

* Sat Dec 15 2007 J. Krebs <rpm_speedy@yahoo.com> - 2:8.8-1
- new version.

* Sun Nov 25 2007 J. Krebs <rpm_speedy@yahoo.com> - 2:8.7-1
- new version.

* Sat Oct 27 2007 J. Krebs <rpm_speedy@yahoo.com> - 2:8.4-1
- new version.

* Tue Aug 21 2007 J. Krebs <rpm_speedy@yahoo.com> - 2:8.3-1
- initial build.
