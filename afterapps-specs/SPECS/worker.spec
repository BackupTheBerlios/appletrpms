%define name worker
%define version 2.15.0
%define release 1%{?dist}
%define doc_version 2.10.0.2

Summary:	A file manager for X in AMIGA style
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Applications/File
Source0:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{version}.tar.gz
Source1:	http://www.boomerangsworld.de/worker/downloads/%{name}-%{doc_version}-doc.tar.bz2
Source2:	worker.desktop
Source3:	worker.png
URL:		http://www.boomerangsworld.de/worker/
BuildRequires:	libX11-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Worker is a graphical filemanager for the X Window System. It uses the
classical two-panel-view of the files and directories. It has many
intern operations while any extern program can also be used for
operate on the selected items. You can easily add actions to filetypes
or buttons with the builtin configuration program.

%prep
%setup -q -a 1

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/

cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
cd worker-%{doc_version}-doc

./configure --prefix=%{_prefix}
make


make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README NEWS AUTHORS ChangeLog
%docdir %{_datadir}/doc/worker
%{_datadir}/doc/worker/*
%{_bindir}/*
%dir %{_datadir}/worker
%{_datadir}/worker/scripts/*
%{_datadir}/worker/catalogs/*
%{_datadir}/worker/config-*
%{_mandir}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Fri Jun 08 2007 J. Krebs <rpm_speedy@yahoo.com> 2.15.0-1
- new version

* Wed Apr 11 2007 J. Krebs <rpm_speedy@yahoo.com> 2.14.4-1
- new version

* Thu Sep 15 2006 J. Krebs <rpm_speedy@yahoo.com> 2.14.0-1
- new version

* Wed Nov 09 2005 J. Krebs <rpm_speedy@yahoo.com> 2.11.0-1
- new version

* Thu Jul 28 2005 J. Krebs <rpm_speedy@yahoo.com> 2.10.2-1
- new version

* Tue Jun 28 2005 J. Krebs <rpm_speedy@yahoo.com> 2.10.1-1
- new version

* Mon May 30 2005 J. Krebs <rpm_speedy@yahoo.com> 2.10.0-1
- new version

* Mon Feb 28 2005 J. Krebs <rpm_speedy@yahoo.com> 2.9.0-1
- new version
