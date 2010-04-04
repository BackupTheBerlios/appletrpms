%define pythtst	%(rpm -q --queryformat='%{VERSION}' python | cut -b1-3)
%define pythver	%pythtst

%define	name 	medit
%define	version	0.10.1
%define	release	1%{?dist}

Summary:	medit is a GTK-based text editor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2 and LGPLv2.1
Group:		Applications/Editors
URL:		http://mooedit.sourceforge.net/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/mooedit/medit/%{version}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-static+man.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	python >= %{pythver}, pcre >= 7.0, libxml2, pygtk2, pango, gtk2, cairo, atk, libICE, libX11, libSM
Buildrequires:	python-devel, pcre-devel >= 7.0, libxml2-devel, perl-XML-Parser, pygtk2-devel, pango-devel 
Buildrequires:	gtk2-devel, cairo-devel, atk-devel, libICE-devel, libX11-devel, libSM-devel, intltool, cmake
BuildRequires:	gettext
Provides:	mooedit

%description
medit is a GTK-based text editor.

%prep
%setup -q
%patch0

%build
%cmake \
	-DMOO_DOC_DIR:PATH=share/doc/%{name}-%{version} \
	-DCMAKE_INSTALL_PREFIX=/usr .
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang moo

%find_lang moo-gsv

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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

%files -f moo.lang
%files -f moo-gsv.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.GPL INSTALL LICENSE NEWS README THANKS doc/help/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/medit.png
%{_datadir}/moo/
%{_datadir}/pixmaps/medit.png
%{_mandir}/man1/medit.*

%changelog
* Sat Mar 20 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.10.1-1
- new version.

* Fri Nov 20 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-3
- added test for python major version.

* Sat Aug 01 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-2
- build patches for FC11.

* Fri Aug 29 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.4-1
- New version.

* Wed Aug 06 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.3-2
- Added libdir to configure for build under x86_64.

* Sun Feb 10 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.3-1
- New version.

* Thu Jan 10 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.9.2-1
- New version.

* Mon Dec 03 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.9.0-1
- Initial build.
