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

%define		name wmwifi
%define		version 0.6
%define		release 5%{?dist}

Summary:	WiFi dockapp displays signal, link, noise, & bitrate info in LCD format
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/222
Source0:	http://dockapps.windowmaker.org/download.php/id/669/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-wireless.c.patch
Patch1:		%{name}-%{version}-%{name}.h.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%if %{mdk}
Requires:	libdockapp0
BuildRequires:	libdockapp0-devel
%endif

%if %{fedora}
Requires:	libdockapp
BuildRequires:	libdockapp-devel
%endif

%description
This dockapp displays the signal strength, link level, noise level, and
bitrate to your current access point. It also displays the current access
point's name.
 
%prep
%setup -q
%patch0
%patch1

%build
./configure --prefix=%{_prefix} --with-x --mandir=%{_mandir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

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
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.6-5
- shifted URLs to http://dockapps.windowmaker.org.

* Mon Aug 23 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.6-4
- changed URL info to dockapps.org.

* Thu Jun 14 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-3
- updated URL info.

* Thu Jun 14 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.6-2
- fixed IFNAMSIZ build issues under FC6.

* Mon Apr 17 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1
- new version.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.5-2
- changed prefix path to /usr.

* Sun Jun 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5-1
- Initial build.
