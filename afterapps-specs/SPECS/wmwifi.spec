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

%define prefix /usr
%define name wmwifi
%define version 0.5
%define release 2

Summary: WiFi dockapp displays signal, link, noise, & bitrate info in LCD format
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmwifi.digitalssg.net/
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}.c.patch
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
%patch0

%build
./configure --prefix=%prefix --with-x
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1/
install -m 644 wmwifi.1 $RPM_BUILD_ROOT%prefix/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README


%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5-2
- changed prefix path to /usr.

* Sun Jun 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5-1
- Initial build.

