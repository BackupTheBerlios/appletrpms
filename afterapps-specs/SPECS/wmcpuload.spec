%define prefix /usr/X11R6
%define name wmcpuload
%define version 1.1.0
%define release 1

Summary: CPU monitor dockapp which has an LCD look user interface
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.sh.rim.or.jp/~ssato/dockapp/index.shtml#wmcpuload
Source0: %{name}-%{version}pre4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}pre4-%{release}-buildroot

%description
WMCPULoad is a CPU monitor dockapp which has an LCD look-alike
user interface, and displays the current usage, expressed as a
percentile and a chart, The back-light may be turned on/off by
clicking the mouse button over the application. If the CPU usage
hits a certain threshold, an alarm-mode will alert you by turning
back-light on. 

%prep
%setup -q -n %{name}-%{version}pre4

%build
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 src/wmcpuload $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO


%changelog
* Mon Feb 21 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0pre4-1
- Initial build.



