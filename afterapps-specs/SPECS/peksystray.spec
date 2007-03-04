### BEGIN Distro Defines
### mdk, fedora, suse & generic are distros
### mandriva, fedoragcc4, and susegcc4 define gcc 4.0 compilers
%define mdk  %(if [ -e /etc/mandrake-release -o -e /etc/mandriva-release ]; then echo 1; else echo 0; fi;)
%{?_with_mdk:   %{expand: %%global mdk 1}}

%define mandriva  %(if [ -e /etc/mandriva-release ]; then echo 1; else echo 0; fi;)
%{?_with_mandriva:   %{expand: %%global mandriva 1}}

%define fedora  %(if [ -e /etc/fedora-release ]; then echo 1; else echo 0; fi;)
%{?_with_fedora:   %{expand: %%global fedora 1}}

%define suse %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi;)
%{?_with_suse:   %{expand: %%global suse 1}}

%define generic 1
%define xseven 0
 
%if %{mdk}
  %define generic 0
%endif

%if %{fedora}
  %define generic 0
  %define xtest $(grep release /etc/fedora-release | cut -d ' ' -f4)
  %define xseven %(if [ %xtest -ge 5 ]; then echo 1; else echo 0; fi;)
  %{?_with_xseven:   %{expand: %%global xseven 1}}
%endif

%if %{suse}
  %define generic 0
%endif

%define prefix /usr
%define name peksystray
%define version 0.4.0
%define release 1

Summary: peksystray is a dockable systray
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://sourceforge.net/projects/peksystray/
Source0: http://easynews.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PekSysTray is a system tray "notification area" dockapp similar to the GNOME
notification area applet. But it's designed for any window manager supporting 
docking.

%prep
%setup -q

%build

%if %{xseven}
	CFLAGS="-lX11" \
	./configure --prefix=%prefix
%else
	./configure --prefix=%prefix
%endif

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 src/peksystray $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
* Fri Feb 16 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.0-1
- New version.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-5
- updated URL and Source info.

* Wed May 25 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-4
- changed to build with FC5 (X11R7).

* Wed Apr  5 2006 Sean Dague <sean@dague.net> - 0.3.0-3
- remove -lX11 which was breaking things

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-2
- changed prefix path to /usr.

* Sat Dec 03 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.3.0-1
- New version.

* Tue Mar 29 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.2.1-1
- Initial build.
