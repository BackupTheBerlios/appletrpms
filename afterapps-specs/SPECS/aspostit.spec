%define prefix /usr/X11R6
%define name aspostit
%define version 1.3
%define release 1

Summary: Post-It notes
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://afterstep.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A swallowable applet allows you to ceate notes in post-it like
style.  The notesare saved in your home directory and are
automatically loaded on the next startup.

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
%doc BUGS CHANGES INSTALL


%changelog
* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.3-1
- Initial build.



