### BEGIN Distro Defines
%define mdk  %(if [ -e /etc/mandrake-release ]; then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1

%if %{mdk}
  %define generic 0
%endif

%if %{fedora}
  %define generic 0
%endif

%if %{suse}
  %define generic 0
%endif
### END Distro Definitions

%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmwifi
%define version 0.6
%define release 1

Summary: WiFi dockapp displays signal, link, noise, & bitrate info in LCD format
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmwifi.digitalssg.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %{mdk}
Requires: libdockapp0
%endif

%if %{fedora}
Requires: libdockapp
%endif

%description
This dockapp displays the signal strength, link level, noise level, and
bitrate to your current access point. It also displays the current access
point's name.
 
%prep
%setup -q

%build
./configure --prefix=%{__prefix} --with-x --mandir=%{_mandir}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 wmwifi.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README


%changelog
* Mon Apr 17 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1
- new version.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5-2
- changed prefix path to /usr.

* Sun Jun 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5-1
- Initial build.
