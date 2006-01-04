%define prefix /usr/X11R6
%define name wmcalc
%define version 0.4
%define release 2

Summary: Wmcalc is an applet calculator.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.dockapps.com/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Wmcalc is a 64x64 pixel application that performs all the
functions (and eventually more) of a simple four function
calculator. It includes a 10 digit alpha-numeric display,
and twenty buttons for user input. Clicking on the display
will clear the calculator.

%prep
%setup -q -n wmcalc-%{version}

%build
#./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin

install -s -m 755 wmcalc $RPM_BUILD_ROOT%prefix/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc COPYING README wmcalc.conf .wmcalc


%changelog
* Wed Jan 04 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4-2
- Included additional tarball config file.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4-1
- Initial build.



