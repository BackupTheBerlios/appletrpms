%define prefix /usr/X11R6
%define name wmpower
%define version 0.4.1
%define release 1

Summary: wmpower is a dockapp to see the power management of a laptop 
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmpower.sourceforge.net/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
wmpower is a Window Maker dock application allowing the user to
graphically see (and set) the power management status of his laptop.

%prep
%setup -q

%build
./configure --exec-prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 src/wmpower $RPM_BUILD_ROOT%prefix/bin
strip $RPM_BUILD_ROOT%prefix/bin/wmpower

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README README.compal THANKS TODO


%changelog
* Sat Feb 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.1-1
- Initial build.



