Summary: wmflame is a WindowMaker dock applet that draws flames
%define version 0.60
Name: wmflame
Version: %{version}
Release: 1
Copyright: GPL
Group: User Interface/Desktops
Source: http://www.reed.edu/~turnerd/programs/%{name}-%{version}.tar.gz
Packager: Ian Macdonald <ianmacd@xs4all.nl>
BuildRoot: /var/tmp/%{name}-root

%description
wmflame makes an animated flame.  The flame algorithm is very standard.  
It is intended for a windowmaker/afterstep dock/wharf applet.

%prep
%setup -n %{name}.app

%build
cd %{name}
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT/usr/X11R6/bin

%files
%defattr(-,root,root)
/usr/X11R6/bin/%{name}
%doc BUGS COPYING INSTALL README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 27 1999 Ian Macdonald <ianmacd@xs4all.nl>

- first RPM release
