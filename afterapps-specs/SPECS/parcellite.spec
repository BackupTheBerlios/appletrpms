%define name parcellite
%define version 0.9.1
%define release 1%{?dist}

Summary: Parcellite (Parcelle Lite) is a lightweight GTK+ clipboard manager
Name: %name
Version: %version
Release: %release
License: GPLv3+
Group: Applications/X11
URL: http://code.google.com/p/xyhthyx/
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: gtk2 >= 2.10
Buildrequires: gtk2-devel >= 2.10

%description
Parcellite (Parcelle Lite) is a lightweight GTK+ clipboard manager. This is
a stripped down, basic-features-only version of Parcelle with a small memory
footprint for those who like simplicity.

%prep
%setup -q

%build
./autogen.sh

./configure --prefix=%{_prefix} --exec_prefix=%{_prefix} --sysconfdir=%{_sysconfdir}

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} exec_prefix=%{_prefix}

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=Parcellite
Name[en_US]=Parcellite
Comment=Lightweight GTK+ clipboard manager
Exec=parcellite
Icon=stock_paste
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                   \
  --add-category GNOME                                            \
  --add-category Application                                      \
  --add-category Utility					  \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/de/LC_MESSAGES/parcellite.mo
%{_datadir}/locale/es/LC_MESSAGES/parcellite.mo
%{_datadir}/locale/hu/LC_MESSAGES/parcellite.mo
%{_datadir}/locale/ja/LC_MESSAGES/parcellite.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/parcellite.mo
%{_datadir}/locale/sv/LC_MESSAGES/parcellite.mo
%{_sysconfdir}/xdg/autostart/parcellite-startup.desktop
%{_mandir}/man1/*

%changelog
* Thu Aug 06 2009 J. Krebs <rpm_speedy@yahoo.com> - 0.9.1-1
- New version.

* Fri Apr 19 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.7-1
- New version.

* Sun Feb 24 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.6.1-1
- New version.

* Sun Feb 10 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1
- New version.

* Mon Jan 21 2008 J. Krebs <rpm_speedy@yahoo.com> - 0.5.1-1
- New version.

* Sun Dec 16 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4.1-1
- New version.

* Sun Nov 25 2007 J. Krebs <rpm_speedy@yahoo.com> - 0.4-1
- Initial build.



