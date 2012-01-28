%define		name wminfo
%define		version 2.5.2
%define		release 1%{?dist}

Summary:	dockapp that displays text-format information using the plugin 
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://linux-bsd-unix.strefa.pl/index.en.html
Source0:	http://linux-bsd-unix.strefa.pl/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-configure.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
%patch0

%build
cd wminfo

./configure --prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

cd wminfo

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog Plugins-HOWTO README README.Privacy TODO
%{_bindir}/cp1250-up2low
%{_bindir}/cp1251-up2low
%{_bindir}/default.wmi
%{_bindir}/empty.wmi
%{_bindir}/html-iso1
%{_bindir}/iso1-up2low
%{_bindir}/iso2-up2low
%{_bindir}/iso5-up2low
%{_bindir}/koi8r-up2low
%{_bindir}/plugin
%{_bindir}/punctuation
%{_bindir}/suspend
%{_bindir}/up2low
%{_bindir}/utf8-iso1
%{_bindir}/utf8-iso2
%{_bindir}/utf8-iso5
%{_bindir}/utf8-up2low
%{_bindir}/wminfo
%{_datadir}/doc/wminfo/contrib/cp1250-up2low
%{_datadir}/doc/wminfo/contrib/cp1251-up2low
%{_datadir}/doc/wminfo/contrib/default.wmi
%{_datadir}/doc/wminfo/contrib/empty.wmi
%{_datadir}/doc/wminfo/contrib/html-iso1
%{_datadir}/doc/wminfo/contrib/iso1-up2low
%{_datadir}/doc/wminfo/contrib/iso2-up2low
%{_datadir}/doc/wminfo/contrib/iso5-up2low
%{_datadir}/doc/wminfo/contrib/koi8r-up2low
%{_datadir}/doc/wminfo/contrib/plugin
%{_datadir}/doc/wminfo/contrib/punctuation
%{_datadir}/doc/wminfo/contrib/README.contrib
%{_datadir}/doc/wminfo/contrib/suspend
%{_datadir}/doc/wminfo/contrib/up2low
%{_datadir}/doc/wminfo/contrib/utf8-iso1
%{_datadir}/doc/wminfo/contrib/utf8-iso2
%{_datadir}/doc/wminfo/contrib/utf8-iso5
%{_datadir}/doc/wminfo/contrib/utf8-up2low
%{_datadir}/doc/wminfo/plugins.offline/arch-patches.wmi
%{_datadir}/doc/wminfo/plugins.offline/bbc-mundo.wmi
%{_datadir}/doc/wminfo/plugins.offline/billboard-top10.wmi
%{_datadir}/doc/wminfo/plugins.offline/cnet.wmi
%{_datadir}/doc/wminfo/plugins.offline/commentcamarche.wmi
%{_datadir}/doc/wminfo/plugins.offline/currencies-pl-avg.wmi
%{_datadir}/doc/wminfo/plugins.offline/currencies-pl-buy.wmi
%{_datadir}/doc/wminfo/plugins.offline/currencies-pl-sell.wmi
%{_datadir}/doc/wminfo/plugins.offline/dockapps.wmi
%{_datadir}/doc/wminfo/plugins.offline/dpreview.wmi
%{_datadir}/doc/wminfo/plugins.offline/freshmeat.wmi
%{_datadir}/doc/wminfo/plugins.offline/kernel-2.4.wmi
%{_datadir}/doc/wminfo/plugins.offline/kernel-2.6.wmi
%{_datadir}/doc/wminfo/plugins.offline/kernel-3.0.wmi
%{_datadir}/doc/wminfo/plugins.offline/linuxquestions.wmi
%{_datadir}/doc/wminfo/plugins.offline/nasdaq.wmi
%{_datadir}/doc/wminfo/plugins.offline/online
%{_datadir}/doc/wminfo/plugins.offline/pitchfork.wmi
%{_datadir}/doc/wminfo/plugins.offline/README.1st.plugins.offline
%{_datadir}/doc/wminfo/plugins.offline/README.weather.wmi
%{_datadir}/doc/wminfo/plugins.offline/run-all-internet-plugins
%{_datadir}/doc/wminfo/plugins.offline/russia-online.wmi
%{_datadir}/doc/wminfo/plugins.offline/slackbuilds.wmi
%{_datadir}/doc/wminfo/plugins.offline/slackware-patches.wmi
%{_datadir}/doc/wminfo/plugins.offline/slashdot.wmi
%{_datadir}/doc/wminfo/plugins.offline/spiegel.wmi
%{_datadir}/doc/wminfo/plugins.offline/tvn24.wmi
%{_datadir}/doc/wminfo/plugins.offline/weather.wmi
%{_datadir}/doc/wminfo/plugins.offline/wyborcza.wmi
%{_datadir}/doc/wminfo/plugins.online/arch-patches.wmi
%{_datadir}/doc/wminfo/plugins.online/bbc-mundo.wmi
%{_datadir}/doc/wminfo/plugins.online/billboard-top10.wmi
%{_datadir}/doc/wminfo/plugins.online/cnet.wmi
%{_datadir}/doc/wminfo/plugins.online/commentcamarche.wmi
%{_datadir}/doc/wminfo/plugins.online/currencies-pl-avg.wmi
%{_datadir}/doc/wminfo/plugins.online/currencies-pl-buy.wmi
%{_datadir}/doc/wminfo/plugins.online/currencies-pl-sell.wmi
%{_datadir}/doc/wminfo/plugins.online/dockapps.wmi
%{_datadir}/doc/wminfo/plugins.online/dpreview.wmi
%{_datadir}/doc/wminfo/plugins.online/freshmeat.wmi
%{_datadir}/doc/wminfo/plugins.online/kernel-2.4.wmi
%{_datadir}/doc/wminfo/plugins.online/kernel-2.6.wmi
%{_datadir}/doc/wminfo/plugins.online/kernel-3.0.wmi
%{_datadir}/doc/wminfo/plugins.online/linuxquestions.wmi
%{_datadir}/doc/wminfo/plugins.online/nasdaq.wmi
%{_datadir}/doc/wminfo/plugins.online/pitchfork.wmi
%{_datadir}/doc/wminfo/plugins.online/README.1st.plugins.online
%{_datadir}/doc/wminfo/plugins.online/README.weather.wmi
%{_datadir}/doc/wminfo/plugins.online/run-all-internet-plugins
%{_datadir}/doc/wminfo/plugins.online/russia-online.wmi
%{_datadir}/doc/wminfo/plugins.online/slackbuilds.wmi
%{_datadir}/doc/wminfo/plugins.online/slackware-patches.wmi
%{_datadir}/doc/wminfo/plugins.online/slashdot.wmi
%{_datadir}/doc/wminfo/plugins.online/spiegel.wmi
%{_datadir}/doc/wminfo/plugins.online/tvn24.wmi
%{_datadir}/doc/wminfo/plugins.online/weather.wmi
%{_datadir}/doc/wminfo/plugins.online/wyborcza.wmi
%{_datadir}/doc/wminfo/plugins.system/alarm
%{_datadir}/doc/wminfo/plugins.system/alarm.txt
%{_datadir}/doc/wminfo/plugins.system/alarm.wmi
%{_datadir}/doc/wminfo/plugins.system/biff.wmi
%{_datadir}/doc/wminfo/plugins.system/date-pl
%{_datadir}/doc/wminfo/plugins.system/date-pl.txt
%{_datadir}/doc/wminfo/plugins.system/date-pl.wmi
%{_datadir}/doc/wminfo/plugins.system/date-us
%{_datadir}/doc/wminfo/plugins.system/date-us.txt
%{_datadir}/doc/wminfo/plugins.system/date-us.wmi
%{_datadir}/doc/wminfo/plugins.system/date.wmi
%{_datadir}/doc/wminfo/plugins.system/df.wmi
%{_datadir}/doc/wminfo/plugins.system/ip.wmi
%{_datadir}/doc/wminfo/plugins.system/netmon
%{_datadir}/doc/wminfo/plugins.system/netmon.wmi
%{_datadir}/doc/wminfo/plugins.system/pinboard
%{_datadir}/doc/wminfo/plugins.system/pinboard.wmi
%{_datadir}/doc/wminfo/plugins.system/ps.wmi
%{_datadir}/doc/wminfo/plugins.system/README.1st.plugins.system
%{_datadir}/doc/wminfo/plugins.system/README.alarm
%{_datadir}/doc/wminfo/plugins.system/README.biff.wmi
%{_datadir}/doc/wminfo/plugins.system/README.CPU.usage
%{_datadir}/doc/wminfo/plugins.system/README.date-xx
%{_datadir}/doc/wminfo/plugins.system/README.netmon.wmi
%{_datadir}/doc/wminfo/plugins.system/README.sysmon.wmi
%{_datadir}/doc/wminfo/plugins.system/README.thinkpad.wmi
%{_datadir}/doc/wminfo/plugins.system/run-all-system-plugins
%{_datadir}/doc/wminfo/plugins.system/sysmon
%{_datadir}/doc/wminfo/plugins.system/sysmon.wmi
%{_datadir}/doc/wminfo/plugins.system/thinkpad.wmi
%{_datadir}/doc/wminfo/plugins.system/top.wmi
%{_datadir}/doc/wminfo/plugins.system/uptime.wmi
%{_datadir}/doc/wminfo/samples/quick-koi8r-dummy.wmi
%{_datadir}/doc/wminfo/samples/quick-koi8r.html
%{_datadir}/doc/wminfo/samples/quick-koi8r-iso5.wmi
%{_datadir}/doc/wminfo/samples/quick-utf8-dummy.wmi
%{_datadir}/doc/wminfo/samples/quick-utf8.html
%{_datadir}/doc/wminfo/samples/quick-utf8-iso1.wmi
%{_datadir}/doc/wminfo/samples/quick-utf8-iso2.wmi
%{_datadir}/doc/wminfo/samples/quick-utf8-iso5.wmi
%{_datadir}/doc/wminfo/samples/README.samples
%{_datadir}/doc/wminfo/samples/run-all-samples
%{_datadir}/doc/wminfo/samples/test-01-50.wmi
%{_datadir}/doc/wminfo/samples/test-50-01.wmi
%{_datadir}/doc/wminfo/samples/test.html
%{_mandir}/man1/wminfo.1.gz

%changelog
* Thu Jan 26 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.5.2-1
- Initial build.
