%define version 2.46
%define release 1%{?dist}
%define name	tkirc

Summary:	tk graphical user interface for the epic Internet Relay Chat (IRC)
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://www.netsplit.de/tkirc2/
Source0:	http://netsplit.de/tkirc2/%{name}%{version}.tar.gz
Source1:	%{name}-%{version}-netsplit.png
Source2:	%{name}-%{version}-browser.sh
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-rc-example.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	epic
Requires:	tk
Provides:	tkirc2
BuildArch:	noarch

%description
Tkirc is a graphical frontend for the ircII or epic textmode IRC
clients. It is written in Tcl/Tk and thus can be greatly configured,
customized and extended.

%prep
%setup -n tkirc2
%patch0
%patch1

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/tkirc/.tkirc2/.data
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/tkirc/.tkirc2/autoload
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/tkirc/.tkirc2/scripts

install -m 755 tkirc2 $RPM_BUILD_ROOT%{_bindir}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-netsplit.png
install -m 644 .tkirc2/scripts/*.tcl $RPM_BUILD_ROOT%{_datadir}/doc/tkirc/.tkirc2/scripts/
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/doc/tkirc/.tkirc2/browser.sh
install -m 644 .tkirc2/tkircrc-example $RPM_BUILD_ROOT%{_datadir}/doc/tkirc/.tkirc2/

ln -sf tkirc2 $RPM_BUILD_ROOT%{_bindir}/tkirc

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=%{name} IRC client
Comment=graphical user interface for the Internet Relay Chat (IRC)
Exec=%{name}2
Icon=tkirc-netsplit.png
Terminal=false
Type=Application" > %{name}.desktop
                                                                                
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category Application                                      \
  --add-category Network                                       \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING README
%{_bindir}/tkirc
%{_bindir}/tkirc2
%{_datadir}/applications/tkirc.desktop
%{_datadir}/doc/tkirc/.tkirc2/.data
%{_datadir}/doc/tkirc/.tkirc2/autoload
%{_datadir}/doc/tkirc/.tkirc2/browser.sh
%{_datadir}/doc/tkirc/.tkirc2/scripts/crazy1.tcl
%{_datadir}/doc/tkirc/.tkirc2/scripts/crazy2.tcl
%{_datadir}/doc/tkirc/.tkirc2/scripts/crazy3.tcl
%{_datadir}/doc/tkirc/.tkirc2/scripts/examples.tcl
%{_datadir}/doc/tkirc/.tkirc2/scripts/hilo.tcl
%{_datadir}/doc/tkirc/.tkirc2/scripts/sound.tcl
%{_datadir}/doc/tkirc/.tkirc2/tkircrc-example
%{_datadir}/pixmaps/tkirc-netsplit.png

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.46-1
- initial build.
