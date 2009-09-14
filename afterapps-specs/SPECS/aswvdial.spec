%define name aswvdial
%define version 1.7
%define release 6%{?dist}

Summary: ASwvdial is a dock/wharf/slit app for wvdial
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/
Source0: ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libxml-devel
Requires: libxml wvdial

%description
ASwvdial is a dock/wharf/slit app for wvdial.

%prep
%setup -q -n aswvdial

%build
#./configure --prefix=%{_prefix}
cd aswvdial
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -s -m 755 aswvdial/aswvdial $RPM_BUILD_ROOT%{_bindir}
install -m 755 aswvdial/netdown $RPM_BUILD_ROOT%{_bindir}
install -m 755 aswvdial/netup $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc COPYING ChangeLog INSTALL README XPM.readme


%changelog
* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.7-6
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.7-5
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.7-4
- changed prefix path to /usr.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-3
- Maker script files install better.

* Sun Jun 12 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-2
- Added require for wvdial (duh).

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.7-1
- Initial build.
