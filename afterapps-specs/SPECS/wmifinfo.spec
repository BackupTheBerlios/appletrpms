%define		name wmifinfo
%define		version 0.09
%define		release 7%{?dist}

Summary:	wmifinfo shows basic network info for all available interfaces
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://www.zevv.nl/play/code/wmifinfo/
Source0:	http://www.zevv.nl/play/code/%{name}/%{name}-%{version}.tgz
Patch0:		%{name}-%{version}-Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libXpm
BuildRequires:	libXpm-devel

%description
wmifinfo is a simple applet showing basic network info for
all available interfaces. It shows IP address, netmask,
gateway and MAC address.

Left-button click moves to the next interface, right-button
click calls ifup/ifdown scripts. 

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.09-7
- updated package requirements.

* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.09-6
- updated spec file.

* Sat Nov 24 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.09-5
- updated URL info.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.09-4
- added distro info to release.

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.09-3
- Updated Source path.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 0.09-2
- changed prefix path to /usr.

* Mon Mar 28 2005 J. Krebs <rpm_speedy@yahoo.com> - 0.09-1
- Initial build.
