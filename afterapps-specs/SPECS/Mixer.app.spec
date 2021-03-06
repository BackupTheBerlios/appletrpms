%define name Mixer.app
%define version 1.8.0
%define release 7%{?dist}

Summary: WM applet sound mixer based-on Rob Malda's asmixer
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.fukt.bsnet.se/~per/mixer/
Source0: http://www.fukt.bsnet.se/~per/mixer/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc-c++


%description
Mixer.app is a mixer utility for Linux/FreeBSD/OpenBSD systems.
It is designed to be docked in Window Maker. This utility has
three volume controllers that can be configured to handle any
sound source, the default sources are master-, cd- and pcm-volume.
Sound sources can easily be muted and there is also wheel mouse
support.

%prep
%setup -q -n Mixer.app-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 Mixer.app $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc ChangeLog INSTALL README COPYING


%changelog
* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-7
- updated URLs, added build require for c++ (gcc-c++).

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-6
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as5
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as4
- changed prefix path to /usr.

* Sat Jun 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as3
- Updated description to include news of AS 2.1.0 compatibility.

* Mon Mar 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as2
- Added build for two binaries, one standard and one for
- AfterStep.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as1
- Included AfterStep Wharf patch. Probably now broken under WM.

* Thu Feb 05 2005 <speedy> - 1.8.0-1
- Initial build.



