%define pythtst %(rpm -q --queryformat='%{VERSION}' python | cut -b1-3)
%define pythver %pythtst

%define	name 	medit
%define	version	1.1.97
%define	release	1%{?dist}

Summary:	medit is a GTK-based text editor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2, LGPLv2.1+, BSD and MIT License
Group:		Applications/Editors
URL:		http://mooedit.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/mooedit/%{name}/unstable-1.1.9x/%{name}-%{version}-devel.tar.bz2
#Source0:	http://downloads.sourceforge.net/project/mooedit/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	glib2
Requires:	glibc
Requires:	gtk2
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libxml2
Requires:	pango
Requires:	pygtk2
Requires:	python < 3.0
Requires:	python >= %{pythver}
Buildrequires:	atk-devel
Buildrequires:	cairo-devel
Buildrequires:	gettext
Buildrequires:	glib2-devel
Buildrequires:	glibc-devel
Buildrequires:	gtk2-devel
Buildrequires:	intltool
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libxml2-devel
Buildrequires:	pango-devel
Buildrequires:	pygtk2-devel
Buildrequires:	python-devel < 3.0
Buildrequires:	python-devel >= %{pythver}
Buildrequires:	redhat-rpm-config
Provides:	mooedit

%description
medit is a GTK-based text editor.

%prep
#%setup -q
%setup -q -n %{name}-%{version}-devel

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --with-python

make VERBOSE=1 %{?_smp_mflags} \
	LIBS=" -lgmodule-2.0 " \
	MOO_PYTHON_LIB_DIR=%{python_sitelib}/medit-1/python \
	MOO_PYTHON_PLUGIN_DIR=%{python_sitelib}/medit-1/plugins

%install
rm -rf $RPM_BUILD_ROOT

make install MOO_PYTHON_LIB_DIR=%{python_sitelib}/medit-1/python \
	MOO_PYTHON_PLUGIN_DIR=%{python_sitelib}/medit-1/plugins \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang medit-1
%find_lang medit-1-gsv

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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

%files -f medit-1.lang
%files -f medit-1-gsv.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}-1/help/*.html
%{_datadir}/doc/%{name}-1/help/img/prefs-file-filters.png
%{_datadir}/doc/%{name}-1/help/img/prefs-file-selector.png
%{_datadir}/doc/%{name}-1/help/medit.css
%{_datadir}/doc/%{name}-1/help/script/*.html
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/medit-1/context.xml
%{_datadir}/medit-1/filters.xml
%{_datadir}/medit-1/lua/_moo/*.lua
%{_datadir}/medit-1/menu.xml
%{_datadir}/medit-1/language-specs/*.lang
%{_datadir}/medit-1/language-specs/*.xml
%{_datadir}/medit-1/language-specs/check.sh
%{_datadir}/medit-1/language-specs/language2.rng
%dir %{python_sitelib}/medit-1/plugins/
%{python_sitelib}/medit-1/plugins/python.ini
%{python_sitelib}/medit-1/plugins/python.py
%{python_sitelib}/medit-1/plugins/python.pyc
%{python_sitelib}/medit-1/plugins/python.pyo
%{python_sitelib}/medit-1/plugins/terminal.ini
%{python_sitelib}/medit-1/plugins/terminal.py
%{python_sitelib}/medit-1/plugins/terminal.pyc
%{python_sitelib}/medit-1/plugins/terminal.pyo
%dir %{python_sitelib}/medit-1/python/
%{python_sitelib}/medit-1/python/insert_date_and_time.py
%{python_sitelib}/medit-1/python/insert_date_and_time.pyc
%{python_sitelib}/medit-1/python/insert_date_and_time.pyo
%{python_sitelib}/medit-1/python/pyconsole.py
%{python_sitelib}/medit-1/python/pyconsole.pyc
%{python_sitelib}/medit-1/python/pyconsole.pyo
%dir %{python_sitelib}/medit-1/python/medit/
%{python_sitelib}/medit-1/python/medit/__init__.py
%{python_sitelib}/medit-1/python/medit/__init__.pyc
%{python_sitelib}/medit-1/python/medit/__init__.pyo
%{python_sitelib}/medit-1/python/medit/runpython.py
%{python_sitelib}/medit-1/python/medit/runpython.pyc
%{python_sitelib}/medit-1/python/medit/runpython.pyo
%{_mandir}/man1/%{name}.*

%changelog
* Sun Dec 07 2013 J. Krebs <rpm_speedy@yahoo.com> - 1.1.97-1
- new version.

* Fri May 17 2013 J. Krebs <rpm_speedy@yahoo.com> - 1.1.96-1
- new version.

* Tue Nov 27 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.1.92-1
- new version.

* Sun Jul 29 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.1.1-1
- new version.

* Sun Mar 04 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.1.0-1
- new version.

* Sun Oct 23 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.0.5-1
- new version.

* Thu Apr 14 2011 J. Krebs <rpm_speedy@yahoo.com> - 1.0.3-1
- new version.

* Thu Aug 26 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.10.4-3
- changed help file path to comply with Fedora packaging guidelines.

* Fri May 28 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.10.4-2
- added links for libm and libdl.

* Thu Apr 29 2010 J. Krebs <rpm_speedy@yahoo.com> - 0.10.4-1
- new version.

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
