%define	name 	medit
%define	version	0.9.3
%define	release	2%{?dist}

Summary:	medit is a GTK-based text editor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2 and LGPLv2
Group:		Applications/Editors
URL:		http://mooedit.sourceforge.net/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/mooedit/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	python, pcre >= 7.0, libxml2, pygtk2, pango, gtk2, cairo, atk, libICE, libX11, libSM
Buildrequires:	python-devel, pcre-devel >= 7.0, libxml2-devel, perl-XML-Parser, pygtk2-devel, pango-devel 
Buildrequires:	gtk2-devel, cairo-devel, atk-devel, libICE-devel, libX11-devel, libSM-devel

%description
medit is a GTK-based text editor.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --with-python --docdir=%{_datadir}/doc/%{name}-%{version}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/mime/mime.cache

rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-mime-database %{_datadir}/mime &> /dev/null || :

touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :

touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.GPL INSTALL LICENSE NEWS README THANKS doc/help/
%{_bindir}/medit
%{_libdir}/moo/
%{_libdir}/python2.5/
%{_datadir}/applications/medit.desktop
%{_datadir}/icons/hicolor/48x48/apps/medit.png
%{_datadir}/locale/
%{_datadir}/mime/
%{_datadir}/moo/
%{_datadir}/pixmaps/medit.png
%{_mandir}/man1/medit*

%changelog
* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.3-2
- Added libdir to configure for build under x86_64.

* Sun Feb 10 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.3-1
- New version.

* Thu Jan 10 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.2-1
- New version.

* Mon Dec 03 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9.0-1
- Initial build.
