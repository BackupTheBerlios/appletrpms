%define prefix /usr/X11R6
%define name astime
%define version 2.8
%define release 2

Summary: An analog clock
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An analog clock that shows the time, the date and the day of
week.  Highly customizable to satisfy the needs of almost any
user.

%prep
%setup -q

%build
./configure --prefix=%prefix
make

%install
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/man/man1
make AFTER_BIN_DIR=$RPM_BUILD_ROOT%prefix/bin \
    AFTER_MAN_DIR=$RPM_BUILD_ROOT%prefix/man/man1 \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%prefix/man/man1/*
%doc CHANGES INSTALL LICENSE README *.astimerc


%changelog
* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.8-2
- Added example .astimerc to the docs area.

* Thu Feb 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.8-1
- Initial build.



