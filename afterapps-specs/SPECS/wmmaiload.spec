%define		name wmmaiload
%define		version 2.3.0
%define		release 1%{?dist}

Summary:	dockapp to monitor your mbox mail files for new and total mails
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://tnemeth.free.fr/projets/dockapps.html
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-prefix.patch
Patch1:		%{name}-%{version}-checkthread.c.patch
Patch2:		%{name}-%{version}-missingincludes.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	atk
Requires:	cairo
Requires:	fontconfig
Requires:	freetype
Requires:	glib2
Requires:	glibc
Requires:	gtk2
Requires:	libpng
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	openssl
Requires:	pango
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gtk2-devel
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	openssl-devel
BuildRequires:	pango-devel

%description
wmmaiload monitors your mbox mail files for new and total mails.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
./configure --prefix=%{_prefix} 

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog FAQ README THANKS TODO doc/sample.wmmailoadrc
%{_bindir}/wmmaiload
%{_bindir}/wmmaiload-config
%{_mandir}/man1/wmmaiload-config.*
%{_mandir}/man1/wmmaiload.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.3.0-1
- Initial build
