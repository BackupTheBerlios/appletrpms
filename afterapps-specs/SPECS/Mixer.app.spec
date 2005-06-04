%define prefix /usr/X11R6
%define name Mixer.app
%define version 1.8.0
%define release as3

Summary: WM applet sound mixer based-on Rob Malda's asmixer
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.fukt.bth.se/~per/mixer
Source0: %{name}-%{version}.tar.gz
Patch0: Mixer.app-1.8.0.as.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This WM applet includes two binaries: "Mixer.app" for AfterStep
>= 2.1.0 and WindowMaker (perhaps other window managers too) and
"Mixer.app.as", a version modified to work with AfterStep < 2.1.0.
The AS version has been modified to work under earlier versions of
AfterStep and will not work properly under WindowMaker.

Mixer.app is a mixer utility for Linux/FreeBSD/OpenBSD systems.
It is designed to be docked in Window Maker. This utility has
three volume controllers that can be configured to handle any
sound source, the default sources are master-, cd- and pcm-volume.
Sound sources can easily be muted and there is also wheel mouse
support.

%prep
%setup -q -n Mixer.app-%{version}

%patch0 -p1 -b .as

%build
make

mv -f Mixer.app Mixer.app.as
cp -f Mixer.cc.as Mixer.cc

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 Mixer.app $RPM_BUILD_ROOT%prefix/bin/Mixer.app
install -s -m 755 Mixer.app.as $RPM_BUILD_ROOT%prefix/bin/Mixer.app.as

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc ChangeLog INSTALL README COPYING


%changelog
* Sat Jun 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as3
- Updated description to include news of AS 2.1.0 compatibility.

* Mon Mar 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as2
- Added build for two binaries, one standard and one for
- AfterStep.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.8.0-as1
- Included AfterStep Wharf patch. Probably now broken under WM.

* Thu Feb 05 2005 <speedy> - 1.8.0-1
- Initial build.



