%define		name calcoo
%define		version 1.3.18
%define		release 3%{?dist}

Summary:	RPN and algebraic scientific calculator
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Applications/Scientific
URL:		http://calcoo.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Calcoo is a scientific calculator designed to provide maximum
usability.  The features that make Calcoo better than (at least some)
other calculator programs are:

* Bitmapped button labels and display digits to improve readability.

* No double-function buttons. As the result, you need to click only one 
  button for any operation (except for arc-hyp trigonometric
  functions).

* Undo/redo buttons.

* Copy/paste interaction with X the clipboard.

* Both RPN (reverse Polish notation) and algebraic modes are available

* Tick marks to separate thousands.                                  

* Two memory registers with displays.

* Displays for Y, Z, and T registers.

* It is a purely scientific calculator. There are no buttons for the 
  hexadecimal digits (ABCDEF) and logical operations, which take space
  and distract from "scientific" buttons.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

make %{?_smp_mflags} LIBS=" -lm"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

#Install application link for X-Windows
echo -e "[Desktop Entry]
Name=Calcoo RPN Scientific Calculator
Comment=Perform arithmetic, scientific or financial calculations
Exec=calcoo
Icon=accessories-calculator
Terminal=false
Encoding=UTF-8
Type=Application" > %{name}.desktop
                                                                                
desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category Utility \
  --add-category Calculator \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/calcoo
%{_datadir}/applications/calcoo.desktop
%{_mandir}/man1/calcoo*

%changelog
* Sat Jan 28 2012 J. Krebs <rpm_speedy@yahoo.com> - 1.3.18-3
- updated sourceforge URLs, added desktop entry.

* Thu May 27 2010 J. Krebs <rpm_speedy@yahoo.com> - 1.3.18-2
- added library links to make.

* Mon Aug 20 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3.18-1
- New version.

* Wed Aug 01 2007 J. Krebs <rpm_speedy@yahoo.com> - 1.3.17-1
- New version.

* Sun Mar 26 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.3.16-1
- Initial build.
