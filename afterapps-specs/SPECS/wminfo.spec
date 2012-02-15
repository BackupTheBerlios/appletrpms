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

make %{?_smp_mflags}

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
%{_bindir}/%{name}
%{_bindir}/plugin
%{_bindir}/punctuation
%{_bindir}/suspend
%{_bindir}/up2low
%{_bindir}/utf8-iso1
%{_bindir}/utf8-iso2
%{_bindir}/utf8-iso5
%{_bindir}/utf8-up2low
%{_datadir}/doc/%{name}/contrib/cp1250-up2low
%{_datadir}/doc/%{name}/contrib/cp1251-up2low
%{_datadir}/doc/%{name}/contrib/default.wmi
%{_datadir}/doc/%{name}/contrib/empty.wmi
%{_datadir}/doc/%{name}/contrib/html-iso1
%{_datadir}/doc/%{name}/contrib/iso1-up2low
%{_datadir}/doc/%{name}/contrib/iso1-utf8
%{_datadir}/doc/%{name}/contrib/iso2-up2low
%{_datadir}/doc/%{name}/contrib/iso2-utf8
%{_datadir}/doc/%{name}/contrib/iso5-up2low
%{_datadir}/doc/%{name}/contrib/iso5-utf8
%{_datadir}/doc/%{name}/contrib/koi8r-up2low
%{_datadir}/doc/%{name}/contrib/plugin
%{_datadir}/doc/%{name}/contrib/punctuation
%{_datadir}/doc/%{name}/contrib/README.contrib
%{_datadir}/doc/%{name}/contrib/suspend
%{_datadir}/doc/%{name}/contrib/up2low
%{_datadir}/doc/%{name}/contrib/utf8-iso1
%{_datadir}/doc/%{name}/contrib/utf8-iso2
%{_datadir}/doc/%{name}/contrib/utf8-iso5
%{_datadir}/doc/%{name}/contrib/utf8-up2low
%{_datadir}/doc/%{name}/plugins.conky/conky.conf
%{_datadir}/doc/%{name}/plugins.conky/conky.date.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.moc.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.netmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.patch
%{_datadir}/doc/%{name}/plugins.conky/conky.sysmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.timezone.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.top.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.uptime.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.weather.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.wireless.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.1st.plugins.conky
%{_datadir}/doc/%{name}/plugins.conky/README.conky.date.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.moc.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.netmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.sysmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.timezone.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.top.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.uptime.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.weather.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.wireless.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.CPU.conky.usage
%{_datadir}/doc/%{name}/plugins.conky/run-all-conky-plugins
%{_datadir}/doc/%{name}/plugins.offline/arch-patches.wmi
%{_datadir}/doc/%{name}/plugins.offline/bbc-mundo.wmi
%{_datadir}/doc/%{name}/plugins.offline/billboard-top10.wmi
%{_datadir}/doc/%{name}/plugins.offline/cnet.wmi
%{_datadir}/doc/%{name}/plugins.offline/commentcamarche.wmi
%{_datadir}/doc/%{name}/plugins.offline/currencies-pl-avg.wmi
%{_datadir}/doc/%{name}/plugins.offline/currencies-pl-buy.wmi
%{_datadir}/doc/%{name}/plugins.offline/currencies-pl-sell.wmi
%{_datadir}/doc/%{name}/plugins.offline/dockapps.wmi
%{_datadir}/doc/%{name}/plugins.offline/dpreview.wmi
%{_datadir}/doc/%{name}/plugins.offline/freecode.wmi
#%{_datadir}/doc/%{name}/plugins.offline/freshmeat.wmi
%{_datadir}/doc/%{name}/plugins.offline/kernel-2.4.wmi
%{_datadir}/doc/%{name}/plugins.offline/kernel-2.6.wmi
#%{_datadir}/doc/%{name}/plugins.offline/kernel-3.0.wmi
%{_datadir}/doc/%{name}/plugins.offline/kernel-3.x.wmi
%{_datadir}/doc/%{name}/plugins.offline/kommersant.wmi
%{_datadir}/doc/%{name}/plugins.offline/linuxquestions-slackware.wmi
#%{_datadir}/doc/%{name}/plugins.offline/linuxquestions.wmi
%{_datadir}/doc/%{name}/plugins.offline/nasdaq.wmi
%{_datadir}/doc/%{name}/plugins.offline/online
%{_datadir}/doc/%{name}/plugins.offline/pitchfork.wmi
%{_datadir}/doc/%{name}/plugins.offline/README.1st.plugins.offline
%{_datadir}/doc/%{name}/plugins.offline/README.weather.wmi
%{_datadir}/doc/%{name}/plugins.offline/run-all-internet-plugins
#%{_datadir}/doc/%{name}/plugins.offline/russia-online.wmi
%{_datadir}/doc/%{name}/plugins.offline/slackbuilds.wmi
%{_datadir}/doc/%{name}/plugins.offline/slackware-patches.wmi
%{_datadir}/doc/%{name}/plugins.offline/slashdot.wmi
%{_datadir}/doc/%{name}/plugins.offline/spiegel.wmi
%{_datadir}/doc/%{name}/plugins.offline/tvn24.wmi
%{_datadir}/doc/%{name}/plugins.offline/weather.wmi
%{_datadir}/doc/%{name}/plugins.offline/wyborcza.wmi
%{_datadir}/doc/%{name}/plugins.online/arch-patches.wmi
%{_datadir}/doc/%{name}/plugins.online/bbc-mundo.wmi
%{_datadir}/doc/%{name}/plugins.online/billboard-top10.wmi
%{_datadir}/doc/%{name}/plugins.online/cnet.wmi
%{_datadir}/doc/%{name}/plugins.online/commentcamarche.wmi
%{_datadir}/doc/%{name}/plugins.online/currencies-pl-avg.wmi
%{_datadir}/doc/%{name}/plugins.online/currencies-pl-buy.wmi
%{_datadir}/doc/%{name}/plugins.online/currencies-pl-sell.wmi
%{_datadir}/doc/%{name}/plugins.online/dockapps.wmi
%{_datadir}/doc/%{name}/plugins.online/dpreview.wmi
%{_datadir}/doc/%{name}/plugins.online/freecode.wmi
#%{_datadir}/doc/%{name}/plugins.online/freshmeat.wmi
%{_datadir}/doc/%{name}/plugins.online/kernel-2.4.wmi
%{_datadir}/doc/%{name}/plugins.online/kernel-2.6.wmi
#%{_datadir}/doc/%{name}/plugins.online/kernel-3.0.wmi
%{_datadir}/doc/%{name}/plugins.online/kernel-3.x.wmi
%{_datadir}/doc/%{name}/plugins.online/kommersant.wmi
%{_datadir}/doc/%{name}/plugins.online/linuxquestions-slackware.wmi
#%{_datadir}/doc/%{name}/plugins.online/linuxquestions.wmi
%{_datadir}/doc/%{name}/plugins.online/nasdaq.wmi
%{_datadir}/doc/%{name}/plugins.online/pitchfork.wmi
%{_datadir}/doc/%{name}/plugins.online/README.1st.plugins.online
%{_datadir}/doc/%{name}/plugins.online/README.weather.wmi
%{_datadir}/doc/%{name}/plugins.online/run-all-internet-plugins
#%{_datadir}/doc/%{name}/plugins.online/russia-online.wmi
%{_datadir}/doc/%{name}/plugins.online/slackbuilds.wmi
%{_datadir}/doc/%{name}/plugins.online/slackware-patches.wmi
%{_datadir}/doc/%{name}/plugins.online/slashdot.wmi
%{_datadir}/doc/%{name}/plugins.online/spiegel.wmi
%{_datadir}/doc/%{name}/plugins.online/tvn24.wmi
%{_datadir}/doc/%{name}/plugins.online/weather.wmi
%{_datadir}/doc/%{name}/plugins.online/wyborcza.wmi
%{_datadir}/doc/%{name}/plugins.system/alarm
%{_datadir}/doc/%{name}/plugins.system/alarm.cfg
#%{_datadir}/doc/%{name}/plugins.system/alarm.txt
%{_datadir}/doc/%{name}/plugins.system/alarm.wmi
%{_datadir}/doc/%{name}/plugins.system/biff.wmi
%{_datadir}/doc/%{name}/plugins.system/date-pl
%{_datadir}/doc/%{name}/plugins.system/date-pl.cfg
#%{_datadir}/doc/%{name}/plugins.system/date-pl.txt
%{_datadir}/doc/%{name}/plugins.system/date-pl.wmi
%{_datadir}/doc/%{name}/plugins.system/date-us
%{_datadir}/doc/%{name}/plugins.system/date-us.cfg
#%{_datadir}/doc/%{name}/plugins.system/date-us.txt
%{_datadir}/doc/%{name}/plugins.system/date-us.wmi
%{_datadir}/doc/%{name}/plugins.system/date.wmi
%{_datadir}/doc/%{name}/plugins.system/df.wmi
%{_datadir}/doc/%{name}/plugins.system/ip.wmi
%{_datadir}/doc/%{name}/plugins.system/netmon
%{_datadir}/doc/%{name}/plugins.system/netmon.wmi
%{_datadir}/doc/%{name}/plugins.system/pinboard
%{_datadir}/doc/%{name}/plugins.system/pinboard.wmi
%{_datadir}/doc/%{name}/plugins.system/ps.wmi
%{_datadir}/doc/%{name}/plugins.system/README.1st.plugins.system
#%{_datadir}/doc/%{name}/plugins.system/README.alarm
%{_datadir}/doc/%{name}/plugins.system/README.alarm.wmi
%{_datadir}/doc/%{name}/plugins.system/README.biff.wmi
%{_datadir}/doc/%{name}/plugins.system/README.CPU.usage
#%{_datadir}/doc/%{name}/plugins.system/README.date-xx
%{_datadir}/doc/%{name}/plugins.system/README.date-xx.wmi
%{_datadir}/doc/%{name}/plugins.system/README.netmon.wmi
%{_datadir}/doc/%{name}/plugins.system/README.stopwatch.wmi
%{_datadir}/doc/%{name}/plugins.system/README.sysmon.wmi
%{_datadir}/doc/%{name}/plugins.system/README.thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.system/README.timer.wmi
%{_datadir}/doc/%{name}/plugins.system/README.timezone.wmi
%{_datadir}/doc/%{name}/plugins.system/README.traffic.wmi
%{_datadir}/doc/%{name}/plugins.system/run-all-system-plugins
%{_datadir}/doc/%{name}/plugins.system/stopwatch
%{_datadir}/doc/%{name}/plugins.system/stopwatch.cfg
%{_datadir}/doc/%{name}/plugins.system/stopwatch.wmi
%{_datadir}/doc/%{name}/plugins.system/sysmon
%{_datadir}/doc/%{name}/plugins.system/sysmon.wmi
%{_datadir}/doc/%{name}/plugins.system/thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.system/timer
%{_datadir}/doc/%{name}/plugins.system/timer.cfg
%{_datadir}/doc/%{name}/plugins.system/timer.wmi
%{_datadir}/doc/%{name}/plugins.system/timezone
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.-0100.CET
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.+0500.EST
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.-0530.IST
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.-0900.JST
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.default
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.GMT
%{_datadir}/doc/%{name}/plugins.system/timezone.wmi
%{_datadir}/doc/%{name}/plugins.system/timezone.wmi.00
%{_datadir}/doc/%{name}/plugins.system/timezone.wmi.30
%{_datadir}/doc/%{name}/plugins.system/top.wmi
%{_datadir}/doc/%{name}/plugins.system/traffic
%{_datadir}/doc/%{name}/plugins.system/traffic.wmi
%{_datadir}/doc/%{name}/plugins.system/uptime.wmi
%{_datadir}/doc/%{name}/samples/quick-koi8r-dummy.wmi
%{_datadir}/doc/%{name}/samples/quick-koi8r.html
%{_datadir}/doc/%{name}/samples/quick-koi8r-iso5.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8-dummy.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8.html
%{_datadir}/doc/%{name}/samples/quick-utf8-iso1.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8-iso2.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8-iso5.wmi
%{_datadir}/doc/%{name}/samples/README.samples
%{_datadir}/doc/%{name}/samples/run-all-samples
%{_datadir}/doc/%{name}/samples/test-01-50.wmi
%{_datadir}/doc/%{name}/samples/test-50-01.wmi
%{_datadir}/doc/%{name}/samples/test.html
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Jan 26 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.5.2-1
- Initial build.
