%define		name wmnetload
%define		version 1.3
%define		release 1%{?dist}

Summary:	network interface monitor dockapp for Window Maker
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://dockapps.windowmaker.org/file.php/id/78
Source0:	http://dockapps.windowmaker.org/download.php/id/353/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-rpath-libdockapp.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
Requires:	libdockapp
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libdockapp-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
wmnetload is a network interface monitor dockapp for Window Maker. 
It is designed to fit well with dockapps like wmcpuload and wmmemmon. 
It tracks whether the interface is functioning and displays current 
network interface throughput, along with an auto-scaling graph of 
recent network activity (the graph separates upstream and downstream 
traffic load cleanly without resorting to colors).

%prep
%setup -q
%patch0

%build
./configure --prefix=%{_prefix}

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/wmnetload

%changelog
* Wed Jan 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.3-1
- Initial build.
