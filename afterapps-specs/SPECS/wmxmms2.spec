%define		name wmxmms2
%define		version 0.6
%define		release 1%{?dist}

Summary:	remote-control dockapp for XMMS2
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		AfterStep/Applets
URL:		http://reboli.nl/
Source0:	http://reboli.nl/programs/%{name}-%{version}.tar.bz2
Source1:	%{name}.man
Patch0:		%{name}-%{version}-gcc-DrNo-DrMattDestruction-compatibility.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
Requires:	xmms2 >= 0.7
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	xmms2-devel >= 0.7

%description
WMxmms is a program that runs on Linux under the 
windowmanagers windowmaker or BlackBox. It gives 
the user control over a daemon-program that runs 
in the background called xmms2. Xmms2 is a music 
player with many features and a wide range of 
supported muzic formats like mp3,ogg,mod and wma.

%prep
%setup -q
%patch0

%build
aclocal
autoconf
automake --add-missing

./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/wmxmms2.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO 
%{_bindir}/wmxmms2
%{_mandir}/man1/wmxmms2.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 0.6-1
- Initial build.
