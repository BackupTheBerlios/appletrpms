%define prefix /usr/X11R6
%define name wmwifi
%define version 0.5
%define release 1

%define generic 1
%define fedora 0
%{?_with_fedora:%define fedora 1}
%define mandrake 0
%{?_with_mandrake:%define mandrake 1}
%if %{fedora}
   %define generic 0
%endif
%if %{mandrake}
   %define generic 0
%endif

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

%if %{mandrake}
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
* Sun Jun 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.5-1
- Initial build.

