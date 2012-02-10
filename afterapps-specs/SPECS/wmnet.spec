%define		name wmnet
%define		version 1.06
%define		release 1%{?dist}

Summary:	network dockapp monitor
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/77
Source0:	http://dockapps.windowmaker.org/download.php/id/115/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-rpath-libdockapp.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libX11
Requires:	libXext
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	imake

%description
WMnet is a little X dock.app network monitor for Linux. It was 
originally inspired by that funky program 'tleds' that blinks your 
keyboard LED's in response to net traffic, but its a lot more 
entertaining than that nowadays. It was written with low cpu-usage, 
low memory, and efficient use of screen real-estate in mind.

%prep
%setup -q

%build
xmkmf

make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 wmnet $RPM_BUILD_ROOT%{_bindir}/
install -m 644 wmnet.man $RPM_BUILD_ROOT%{_mandir}/man1/wmnet.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changelog README
%{_bindir}/wmnet
%{_mandir}/man1/wmnet.*

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.06-1
- Initial build.
