%define name asmodem
%define version 0.6
%define release 6%{?dist}

Summary: Modem monitor
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tigr.net/afterstep/view.php?applet=asmodem/data
Source0: http://tigr.net/afterstep/download/%{name}/%{name}-%{version}-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A swallowable applet monitors the modem.

%prep
%setup -q -n %{name}-%{version}-1

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 asmodem $RPM_BUILD_ROOT%{_bindir}
install -m 644 asmodem.man $RPM_BUILD_ROOT%{_mandir}/man1/asmodem.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc INSTALL README


%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> 0.6-6
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> 0.6-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> 0.6-4
- changed prefix path to /usr.

* Sat Feb 26 2005 Sean Dague <sean@dague.net> 0.6-3
- really ugly work around for odd tarball version

* Sat Feb 26 2005 Sean Dague <sean@dague.net> 0.6-1-2
- change to asmodem versioning scheme

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1-1
- Initial build.



