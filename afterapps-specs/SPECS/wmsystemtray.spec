%define		name wmsystemtray
%define		version 1.2
%define		release 2%{?dist}

Summary:	versatile system tray (freedesktop.org systray protocol) Window Maker dock app
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://wmsystemtray.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	libICE
Requires:	libSM
Requires:	libX11
Requires:	libXext
Requires:	libXfixes
Requires:	libXmu
Requires:	libXpm
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXmu-devel
BuildRequires:	libXpm-devel

%description
A system tray (freedesktop.org systray protocol) as a Window Maker
dock app with the ability to display more than just four tray icons.

%prep

%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.2-2
- updated sourceforge URLs.

* Sun Aug 29 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.2-1
- initial build.
