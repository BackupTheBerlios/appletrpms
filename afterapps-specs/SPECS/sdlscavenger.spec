%define version 1.4.5.1_2010_11_5
%define release 1%{?dist}
%define name	sdlscavenger

Summary:	arcade/thinking game very much like Lode Runner
Name:		%name
Version:	%version
Release:	%release
License:	GPLv1
Group:		Amusements/Games
Source0:	http://prdownloads.sourceforge.net/sdlscavenger/sdlscav-145.1_2010_11_5.tgz
Patch0:		%{name}-%{version}-Makefile.patch
Patch1:		%{name}-%{version}-names.h.patch
URL:		http://sourceforge.net/projects/sdlscavenger/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes:	xscavenger
Requires:	SDL_image
Requires:	SDL_gfx
Requires:	SDL_sound
Requires:	SDL
Requires:	bash
Requires:	glibc
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL-devel
Requires:	glibc-devel

%description
Scavenger is a fun 2-D game like Lode Runner. With 193 very good
puzzle screens to solve. Works in linux or Windows using (SDL)
libraries.  Has more than 20 improvements over the original.

%prep
%setup -q -n sdlscav-145
%patch0
%patch1

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=SDL Scavenger
Comment=Lode Runner type arcade game
Exec=sdlscav -w
Icon=
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                   \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Game                                      \
  --add-category ArcadeGame						  \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING CREDITS DOC NEW_FEATURES README STRATEGY changelog
%{_bindir}/scavsaver
%{_bindir}/sdlscav
%{_datadir}/applications/*.desktop
%{_datadir}/sdlscavenger/badguy.lbm
%{_datadir}/sdlscavenger/brownblue.lbm
%{_datadir}/sdlscavenger/death.raw
%{_datadir}/sdlscavenger/death.wav
%{_datadir}/sdlscavenger/devil.xpm
%{_datadir}/sdlscavenger/dig.raw
%{_datadir}/sdlscavenger/dig.wav
%{_datadir}/sdlscavenger/fall.raw
%{_datadir}/sdlscavenger/fall.wav
%{_datadir}/sdlscavenger/highrc
%{_datadir}/sdlscavenger/highstreet.lbm
%{_datadir}/sdlscavenger/leprechaun.lbm
%{_datadir}/sdlscavenger/levels.scl
%{_datadir}/sdlscavenger/masters.scl
%{_datadir}/sdlscavenger/microman.lbm
%{_datadir}/sdlscavenger/microman.xpm
%{_datadir}/sdlscavenger/micromanrc
%{_datadir}/sdlscavenger/pop.raw
%{_datadir}/sdlscavenger/pop.wav
%{_datadir}/sdlscavenger/redbrick.lbm
%{_datadir}/sdlscavenger/reddevil.lbm
%{_datadir}/sdlscavenger/reddevilrc
%{_datadir}/sdlscavenger/regularguy.lbm
%{_datadir}/sdlscavenger/scav.bmp
%{_datadir}/sdlscavenger/scav.png
%{_datadir}/sdlscavenger/scav.xpm
%{_datadir}/sdlscavenger/scavrc
%{_datadir}/sdlscavenger/shamrc
%{_datadir}/sdlscavenger/shamrock.lbm
%{_datadir}/sdlscavenger/shamrock.xpm
%{_datadir}/sdlscavenger/spiral.lbm
%{_datadir}/sdlscavenger/spiralthing.lbm
%{_datadir}/sdlscavenger/victory.raw
%{_datadir}/sdlscavenger/victory.wav

%changelog
* Sun Nov 27 2011 J. Krebs <rpm_speedy@yahoo.com> 1.4.5.18-1
- initial build.
