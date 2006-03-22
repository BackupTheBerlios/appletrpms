%define prefix /usr
%define name wmmsg
%define version 1.0.1
%define release 2

Summary: dockapp that notifies of incoming messages and events
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.dockapps.com/file.php/id/169
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-sounds.tar.gz
Source2: wmmsgrc-example
Source3: %{name}-icons.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: imlib2
BuildRequires: imlib2-devel

%description
wmmsg is a dockapp that informs you of new events, such as
incoming chat messages, by displaying related icons and arrival
times. A notification program, wmmsg_notify, is included to send
events to the dockapp. This can be called from messaging clients,
or any other useful location. Works with Gaim, X-Chat, etc.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
mkdir -p $RPM_BUILD_ROOT%prefix/share/wmmsg/sounds/
mkdir -p $RPM_BUILD_ROOT%prefix/share/wmmsg/icons/

install -s -m 755 wmmsg $RPM_BUILD_ROOT%prefix/bin/
install -s -m 755 wmmsg_notify $RPM_BUILD_ROOT%prefix/bin/
install -m 644 man/*.1 $RPM_BUILD_ROOT%prefix/man/man1/

cp %{SOURCE2} .

cp %{SOURCE1} $RPM_BUILD_ROOT%prefix/share/wmmsg/sounds/
cd $RPM_BUILD_ROOT%prefix/share/wmmsg/sounds/
tar xvzf wmmsg-sounds.tar.gz
rm -f wmmsg-sounds.tar.gz

cp %{SOURCE3} $RPM_BUILD_ROOT%prefix/share/wmmsg/icons/
cd $RPM_BUILD_ROOT%prefix/share/wmmsg/icons/
tar xvzf wmmsg-icons.tar.gz
rm -f wmmsg-icons.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%postun
%prefix/share/wmmsg/sounds/
%prefix/share/wmmsg/icons/

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%prefix/share/wmmsg/sounds/*.wav
%prefix/share/wmmsg/icons/*.png
%doc AUTHORS COPYING ChangeLog INSTALL README plugins/* wmmsgrc-example


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-2
- changed prefix path to /usr.

* Sat Mar 12 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-1
- Initial build.




