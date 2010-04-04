%define name	mined
%define version	2000.16
%define release	1%{?dist}

Summary:	mined is a powerful text editor with extensive Unicode and CJK support
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Applications/Editors
URL:		http://towo.net/mined/
Source0:	http://towo.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	ncurses
Buildrequires:	ncurses-devel

%description
mined is a powerful text editor with extensive Unicode and CJK support.

%prep
%setup -q -n %{name}-2000.15

%build
make -C src -f makefile.linux PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/mined/*
%{_mandir}/man1/*
%doc doc COMPILE.DOC DESCR INSTALL.DOC PACKAGE.DOC README VERSION

%changelog
* Mon Mar 01 2010 J. Krebs <rpm_speedy@yahoo.com> - 2000.16-1
- New version.

* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 2000.15.4-1
- New version.

* Sat Aug 09 2008 J. Krebs <rpm_speedy@yahoo.com> - 2000.14-2
- Added termio patch (from Suse) for build under AMD84.

* Tue Aug 21 2007 J. Krebs <rpm_speedy@yahoo.com> - 2000.14-1
- Initial build.
