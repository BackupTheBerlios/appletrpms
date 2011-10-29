%define		name wmpower
%define		version 0.5.0
%define		release 1%{?dist}

Summary:	wmpower is a dockapp to see the power management of a laptop 
Name:		%name
Version:	%version
Release:	%release
License:	GPLv3+
Group:		AfterStep/Applets
URL:		http://linux-bsd-unix.strefa.pl/index.en.html
Source0:	http://linux-bsd-unix.strefa.pl/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:	i386 i486 i586 i686

%description
wmpower is a Window Maker dock application allowing the user to
graphically see (and set) the power management status of his laptop.

%prep
%setup -q

%build
./configure --exec-prefix=%{_prefix} --prefix=%{_prefix} --includedir=%{_includedir} CPUFLAGS="-march=athlon64"
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 src/wmpower $RPM_BUILD_ROOT%{_bindir}
strip $RPM_BUILD_ROOT%{_bindir}/wmpower

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS BUGS COPYING ChangeLog LEGGIMI NEWS README README.compal THANKS TODO

%changelog
* Sat Oct 10 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.5.0-1
- new ownership, version, and URLs.

* Sat Aug 01 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.4.3-1
- new version.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.2-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.2-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.4.2-2
- changed prefix path to /usr.

* Sat Jul 23 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.2-1
- New version.

* Sat Feb 26 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.4.1-1
- Initial build.
