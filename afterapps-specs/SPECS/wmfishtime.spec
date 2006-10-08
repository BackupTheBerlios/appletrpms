%define __prefix /usr
%define _bindir %{__prefix}/bin
%define _datadir %{__prefix}/share
%define _mandir %{_datadir}/man
%define name wmfishtime
%define version 1.24
%define release 3

Summary: clock dockapp with fish.
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://www.ne.jp/asahi/linux/timecop/
Source0: http://www.ne.jp/asahi/linux/timecop/software/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Well, this is just your standard time dockapp. Top part has the clock face,
bottom part has day of the week, followed by day, followed by month. Yellow
hand counts seconds, green hand counts minutes, red hand counts hours. Few
seconds after startup there are at least 32 bubbles floating up behind the
clock face.  There are 4 fishes randomly swimming back and forth. If you move
your mouse inside the dockapp window, the fish will get scared and run away.
If you compiled in mail checking (default), then whenever you get new mail
in the file pointed to by the $MAIL variable, it will display green weed
partially blocking the day/month counter, to remind you to read your mail.
If $MAIL is not set, nothing happens.

%prep
%setup -q

%build
make PREFIX=%{__prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 755 wmfishtime $RPM_BUILD_ROOT%{_bindir}/
install -m 644 wmfishtime.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc ALL_I_GET_IS_A_GRAY_BOX AUTHORS CODING COPYING ChangeLog INSTALL README


%changelog
* Sat Oct 07 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.24-3
- updated URL and Source info.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.24-2
- changed prefix path to /usr.

* Sat Mar 05 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.24-1
- Initial build.
