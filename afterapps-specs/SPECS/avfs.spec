%define	name 	avfs
%define	version	1.0.0
%define	release	2%{?dist}

Summary:	Enables programs to look inside archived/compressed files, access remote files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and LGPLv2+
Group:		Applications/Archiving
URL:		http://sourceforge.net/projects/avf
Source0:	http://downloads.sourceforge.net/project/avf/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	fuse
Requires:	glibc
Requires:	perl
Buildrequires:	fuse-devel
Buildrequires:	glibc-devel
Buildrequires:	perl-devel

%description
AVFS is a system, which enables all programs to look inside archived
or compressed files, or access remote files without recompiling the
programs or changing the kernel.

At the moment it supports floppies, tar and gzip files, zip, bzip2, ar
and rar files, ftp sessions, http, webdav, rsh/rcp, ssh/scp. Quite a
few other handlers are implemented with the Midnight Commander's
external FS.

%package devel
Summary:   Development libraries and header files for %{name}
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description devel
Development libraries and header files for %{name}

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-fuse
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf doc/Makefil*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README TODO doc/
%{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/*.so.*
%{_includedir}/*

%files devel
%{_includedir}/
%{_libdir}/*.so
%{_libdir}/*.*a

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-2
- updated spec file.

* Tue Jul 19 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.0.0-1
- New version.

* Fri Oct 08 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.9-1
- New version.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.8-2
- Added libdir to configure for build under x86_64.

* Sat Nov 10 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9.8-1
- Initial build.
