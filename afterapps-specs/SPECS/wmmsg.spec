%define name wmmsg
%define version 1.0.1
%define release 5%{?dist}

Summary: dockapp that notifies of incoming messages and events
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://swapspace.net/~matt/wmmsg/
Source0: http://swapspace.net/~matt/wmmsg/%{name}-%{version}.tar.gz
Source1: %{name}-sounds.tar.gz
Source2: wmmsgrc-example
Source3: %{name}-icons.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: imlib2
BuildRequires: imlib2-devel gcc-c++

%description
wmmsg is a dockapp that informs you of new events, such as
incoming chat messages, by displaying related icons and arrival
times. A notification program, wmmsg_notify, is included to send
events to the dockapp. This can be called from messaging clients,
or any other useful location. Works with Gaim, X-Chat, etc.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wmmsg/sounds/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wmmsg/icons/

cp %{SOURCE2} .

cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wmmsg/sounds/
cd $RPM_BUILD_ROOT%{_datadir}/wmmsg/sounds/
tar xvzf wmmsg-sounds.tar.gz
rm -f wmmsg-sounds.tar.gz

cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/wmmsg/icons/
cd $RPM_BUILD_ROOT%{_datadir}/wmmsg/icons/
tar xvzf wmmsg-icons.tar.gz
rm -f wmmsg-icons.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/wmmsg/sounds
%{_datadir}/wmmsg/sounds/*.wav
%dir %{_datadir}/wmmsg/icons
%{_datadir}/wmmsg/icons/*.png
%doc AUTHORS COPYING ChangeLog INSTALL README plugins/* wmmsgrc-example

%changelog
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
