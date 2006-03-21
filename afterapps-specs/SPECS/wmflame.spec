%define prefix /usr
%define name wmflame
%define version 0.60
%define release 3

Summary: wmflame is a WindowMaker dock applet that draws flames
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
Source: http://www.reed.edu/~turnerd/programs/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot

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
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT%{prefix}/bin

%files
%defattr(-,root,root)
%{prefix}/bin/%{name}
%doc BUGS COPYING INSTALL README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.6-3
- changed prefix path to /usr.

* Fri Jun 10 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-2
- replaced "copyright" with "license", updated .spec

* Tue Jul 27 1999 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release
