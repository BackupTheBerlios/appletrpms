%define aitest	%(rpm -q --queryformat='%{VERSION}' libAfterImage)
%define aiver	%aitest 
%define version 9.19
%define release 1%{?dist}
%define name	rxvt-unicode
%define epoch	2

Summary:	unicode version of rxvt
Name:		%name
Version:	%version
Release:	%release
Epoch:		%epoch
License:	GPLv2+
Group:		User Interface/X
URL:		http://software.schmorp.de/pkg/rxvt-unicode.html
Source0:	http://dist.schmorp.de/rxvt-unicode/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	perl-devel libXpm-devel libXft-devel freetype-devel perl-ExtUtils-Embed
BuildRequires:	libAfterImage-devel >= 1.15
BuildRequires:  fontconfig-devel gcc-c++
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

%build

./configure --prefix=%{_prefix} --libdir=%{_libdir} \
		--with-xpm-includes=%{_includedir}/X11 \
		--with-xpm-library=%{_libdir} \
		--enable-afterimage

make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}"

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
Icon=terminal.png
                                                                                
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
%doc COPYING Changes README.FAQ README.configure doc/README.xvt doc/etc doc/changes.txt
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_libdir}/urxvt

%changelog
* Wed Oct 30 2013 J. Krebs <rpm_speedy@yahoo.com> - 2:9.19-1
- new version.

* Thu Jul 18 2013 J. Krebs <rpm_speedy@yahoo.com> - 2:9.18-2
- updated for build against libAfterImage 1.21.

* Tue Apr 02 2013 J. Krebs <rpm_speedy@yahoo.com> - 2:9.18-1
- new version.

* Thu Dec 27 2012 J. Krebs <rpm_speedy@yahoo.com> - 2:9.16-1
- new version.

* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 2:9.15-1
- new version.

* Wed Jan 04 2012 J. Krebs <rpm_speedy@yahoo.com> - 2:9.14-1
- new version.

* Tue Jul 19 2011 J. Krebs <rpm_speedy@yahoo.com> - 2:9.12-1
- new version.

* Mon May 02 2011 J. Krebs <rpm_speedy@yahoo.com> - 2:9.11-1
- new version.

* Thu Dec 16 2010 J. Krebs <rpm_speedy@yahoo.com> - 2:9.10-1
- new version.

* Wed Feb 03 2010 J. Krebs <rpm_speedy@yahoo.com> - 2:9.07-1
- new version.

* Thu Jul 30 2009 J. Krebs <rpm_speedy@yahoo.com> - 2:9.06-1
- new version.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 2:9.05-2
- added required for perl-ExtUtils-Embed.

* Sat Jun 21 2008 J. Krebs <rpm_speedy@yahoo.com> - 2:9.05-1
- new version.

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
