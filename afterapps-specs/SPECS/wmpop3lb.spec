%define prefix /usr/X11R6
%define name wmpop3lb
%define version 2.4.2
%define release 1

Summary: WMPop3LB is a multi POP3 mail box checker
Name: %name
Version: %version
Release: %release
License: GPL
Group: AfterStep/Applets
URL: http://wmpop3lb.jourdain.org/
Source0: %{name}%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WMPop3LB is a multi POP3 mail box checker. It will connect to up to 6
POP3 servers to check if you have mail, get the "From:" and "Subject:"
header fields of each mail and display them in a 7 lines window. 
If there are more than 7 mails, they can be read by scrolling the window 
up and down.
Messages can be deleted directly off the servers by selecting the mails
to delete and clicking the "delete" button.
A command to spawn can be specified for each new received message, for
selected messages (by clicking on the "open" button) or to launch a 
mailclient. 

%prep
%setup -q -n %{name}%{version}

%build
cd wmpop3
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
install -s -m 755 wmpop3/wmpop3lb $RPM_BUILD_ROOT%prefix/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%prefix/bin/*
%doc CHANGE_LOG COPYING INSTALL README wmpop3/.wmpop3rc*


%changelog
* Mon Mar 28 2005 J. Krebs <rpm_speedy@yahoo.com> - 2.4.2-1
- Initial build.


