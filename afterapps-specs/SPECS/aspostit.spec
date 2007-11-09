%define name aspostit
%define version 1.3
%define release 5%{?dist}

Summary: Post-It notes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://tigr.net/afterstep/view.php?applet=aspostit/data
Source0: http://tigr.net/afterstep/download/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libXaw
Buildrequires: libXaw-devel

%description
A swallowable applet allows you to ceate notes in post-it like
style.  The notesare saved in your home directory and are
automatically loaded on the next startup.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc BUGS CHANGES INSTALL


%changelog
* Thu Nov 08 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3-5
- added requires for libXaw.

* Fri Apr 13 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3-4
- added distro info to release.

* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3-2
- changed prefix path to /usr.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.3-1
- Initial build.



