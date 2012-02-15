%define		name mpck
%define		version 0.19
%define		release 1%{?dist}

Summary:	checks mp3 file integrity from the command line
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://www.checkmate.gissen.nl/
Source0:	http://www.checkmate.gissen.nl/checkmate-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	glibc
BuildRequires:	glibc-devel

%description
Checkmate mpck checks mp3s. It scans the file to see if the frames are
where they are supposed to be, if the frame headers are correct  and  if 
the headers are consistent throughout the file. It gives some statistics
on the file like bitrate and length, and a conclusion whether the file is
good or bad.

%prep
%setup -q -n checkmate-%{version}

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/mpck
%{_mandir}/man1/*
%doc ABOUT_FIXING AUTHORS COPYING ChangeLog HISTORY NEWS README TODO

%changelog
* Wed Nov 23 2011 J. Krebs <rpm_speedy@yahoo.com> - 0.19-1
- Initial build.
