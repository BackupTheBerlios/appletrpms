%define		name wmpower+
%define		version 1.0.1
%define		release 1%{?dist}

Summary:	dockapp to see the power management of a laptop 
Name:		%name
Version:	%version
Release:	%release
License:	GPLv3+
Group:		AfterStep/Applets
URL:		http://linux-bsd-unix.strefa.pl/index.en.html
Source0:	http://linux-bsd-unix.strefa.pl/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes:	wmpower
Requires:	glibc
Requires:	libX11
Requires:	libXext
Requires:	libXpm
BuildRequires:	glibc-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel

%description
wmpower is a Window Maker dock application allowing the user to
graphically see (and set) the power management status of his laptop.

%prep
%setup -q

%build
./configure --exec-prefix=%{_prefix} --prefix=%{_prefix} --includedir=%{_includedir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 src/wmpower $RPM_BUILD_ROOT%{_bindir}
strip $RPM_BUILD_ROOT%{_bindir}/wmpower

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc AUTHORS BUGS COPYING ChangeLog NEWS README README.compal THANKS TODO

%changelog
* Mon Jun 25 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.0.1-1
- Initial build.
