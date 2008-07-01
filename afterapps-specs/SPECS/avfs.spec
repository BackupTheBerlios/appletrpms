%define	name 	avfs
%define	version	0.9.8
%define	release	1%{?dist}

Summary:	Enables programs to look inside archived/compressed files, access remote files
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2 and LGPLv2
Group:		Applications/Archiving
URL:		http://sourceforge.net/projects/avf
Source0:	http://easynews.dl.sourceforge.net/sourceforge/avf/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	fuse
Buildrequires:	fuse-devel

%description
AVFS is a system which enables all programs to look inside archived
or compressed files, or access remote files without recompiling the
programs or changing the kernel.

At the moment it supports floppies, tar and gzip files, zip, bzip2, ar
and rar files, ftp sessions, http, webdav, rsh/rcp, ssh/scp. Quite a
few other handlers are implemented with the Midnight Commander's
external FS.

AVFS is (C) under the GNU GPL (see the file COPYING). The shared
library supporting AVFS with LD_PRELOAD is (C) under the GNU LGPL (see
the file COPYING.LIB).

AVFS comes with ABSOLUTELY NO WARRANTY, for details see the file COPYING. 

%package devel
Summary:   Development libraries and header files for %{name}
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description devel
Development libraries and header files for %{name}

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --enable-fuse
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
%{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/*.so.*
%{_includedir}/*
%doc AUTHORS COPYING COPYING.LIB ChangeLog INSTALL NEWS README TODO doc/

%files devel
%{_includedir}/
%{_libdir}/*.so
%{_libdir}/*.*a

%changelog
* Sat Nov 10 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9.8-1
- Initial build.