%define name worker
%define version 2.16.2
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
URL:		http://www.boomerangsworld.de/worker/
Requires:	libXpm avfs fuse
BuildRequires:	libX11-devel bzip2-devel zlib-devel libXpm-devel avfs-devel
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
./configure --prefix=%{_prefix} --mandir=%{_mandir} --docdir=%{_datadir}/doc/%{name}-%{version}
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/

install -m 644 Icons/WorkerIcon16.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/worker.xpm
install -m 644 Icons/WorkerIcon32.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/worker.xpm
install -m 644 Icons/WorkerIcon48.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/worker.xpm
install -m 644 Icons/WorkerIcon.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/worker.xpm

rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/*.xpm

cd worker-%{doc_version}-doc
./configure --prefix=%{_prefix}
make
make DESTDIR=$RPM_BUILD_ROOT install

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=Worker File Manager
Comment=View and manage files
Exec=worker
Icon=worker.xpm
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                   \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category System						  \
  %{name}.desktop

cd ..

mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 AUTHORS $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 COPYING $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 INSTALL $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 ChangeLog $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 NEWS $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 READM* $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
install -m 644 THANKS $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/

mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/* $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files
%defattr(-,root,root,-)
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}/
%{_bindir}/*
%dir %{_datadir}/worker
%{_datadir}/worker/scripts/*
%{_datadir}/worker/catalogs/*
%{_datadir}/worker/config-*
%{_mandir}/
%{_datadir}/icons/hicolor/
%{_datadir}/applications/*

%changelog
* Mon Feb 11 2008 J. Krebs <rpm_speedy@yahoo.com> 2.16.2-1
- new version

* Mon Dec 03 2007 J. Krebs <rpm_speedy@yahoo.com> 2.16.1-1
- new version

* Tue Nov 13 2007 J. Krebs <rpm_speedy@yahoo.com> 2.16.0-1
- new version

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
