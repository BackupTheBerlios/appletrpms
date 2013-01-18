%define		name wminfo
%define		version 4.0.0
%define		release 1%{?dist}

Summary:	dockapp that displays text-format information using the plugin 
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		AfterStep/Applets
URL:		http://linux-bsd-unix.strefa.pl/index.en.html
Source0:	http://linux-bsd-unix.strefa.pl/%{name}-%{version}.tar.gz
Patch0:		%{name}-4.0.0-configure.patch
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
%doc COPYING ChangeLog Plugins-HOWTO README TODO
%{_bindir}/accuweather
%{_bindir}/bash-empty.wmi
%{_bindir}/conky-parser
%{_bindir}/counter
%{_bindir}/default.wmi
%{_bindir}/dos-unix
%{_bindir}/empty.wmi
%{_bindir}/forecast
%{_bindir}/html-iso1
%{_bindir}/html-iso2
%{_bindir}/html-iso5
%{_bindir}/iso1-utf8
%{_bindir}/iso2-utf8
%{_bindir}/iso5-utf8
%{_bindir}/macos-unix
%{_bindir}/%{name}
%{_bindir}/netmon
%{_bindir}/plugin
%{_bindir}/punctuation
%{_bindir}/run-all-wminfo-plugins
%{_bindir}/suspend
%{_bindir}/sysmon
%{_bindir}/time+date
%{_bindir}/traffic
%{_bindir}/utf8-iso1
%{_bindir}/utf8-iso2
%{_bindir}/utf8-iso5
%{_bindir}/weather-
%{_bindir}/weather-poland
%{_bindir}/wminfo-benchmark
%{_bindir}/wminfo-conky
%{_datadir}/doc/%{name}/BUGS
%{_datadir}/doc/%{name}/ChangeLog
%{_datadir}/doc/%{name}/contrib/accuweather
%{_datadir}/doc/%{name}/contrib/bash-empty.wmi
%{_datadir}/doc/%{name}/contrib/conky-parser
%{_datadir}/doc/%{name}/contrib/counter
%{_datadir}/doc/%{name}/contrib/default.wmi
%{_datadir}/doc/%{name}/contrib/dos-unix
%{_datadir}/doc/%{name}/contrib/forecast
%{_datadir}/doc/%{name}/contrib/html-iso1
%{_datadir}/doc/%{name}/contrib/html-iso2
%{_datadir}/doc/%{name}/contrib/html-iso5
%{_datadir}/doc/%{name}/contrib/invocation-counter
%{_datadir}/doc/%{name}/contrib/iso1-utf8
%{_datadir}/doc/%{name}/contrib/iso2-utf8
%{_datadir}/doc/%{name}/contrib/iso5-utf8
%{_datadir}/doc/%{name}/contrib/macos-unix
%{_datadir}/doc/%{name}/contrib/netmon
%{_datadir}/doc/%{name}/contrib/plugin
%{_datadir}/doc/%{name}/contrib/punctuation
%{_datadir}/doc/%{name}/contrib/README.contrib
%{_datadir}/doc/%{name}/contrib/README.plugin
%{_datadir}/doc/%{name}/contrib/README.time+date
%{_datadir}/doc/%{name}/contrib/README.weather-
%{_datadir}/doc/%{name}/contrib/README.wminfo-benchmark
%{_datadir}/doc/%{name}/contrib/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/contrib/suspend
%{_datadir}/doc/%{name}/contrib/sysmon
%{_datadir}/doc/%{name}/contrib/time+date
%{_datadir}/doc/%{name}/contrib/traffic
%{_datadir}/doc/%{name}/contrib/utf8-iso1
%{_datadir}/doc/%{name}/contrib/utf8-iso2
%{_datadir}/doc/%{name}/contrib/utf8-iso5
%{_datadir}/doc/%{name}/contrib/weather-
%{_datadir}/doc/%{name}/contrib/weather-poland
%{_datadir}/doc/%{name}/contrib/wminfo-benchmark
%{_datadir}/doc/%{name}/contrib/wminfo-benchmark-extensive
%{_datadir}/doc/%{name}/contrib/wminfo-benchmark-timings
%{_datadir}/doc/%{name}/contrib/wminfo-conky
%{_datadir}/doc/%{name}/COPYING
%{_datadir}/doc/%{name}/INSTALL
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-01.bin
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-01.c
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-01.wmi
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-02.bin
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-02.c
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-02.wmi
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-03.bin
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-03.c
%{_datadir}/doc/%{name}/plugins.binary/binclock-vertical-03.wmi
%{_datadir}/doc/%{name}/plugins.binary/c-empty.bin
%{_datadir}/doc/%{name}/plugins.binary/c-empty.c
%{_datadir}/doc/%{name}/plugins.binary/c-empty.wmi
%{_datadir}/doc/%{name}/plugins.binary/Makefile
%{_datadir}/doc/%{name}/plugins.binary/README.1st.plugins.binary
%{_datadir}/doc/%{name}/plugins.binary/README.binclock-vertical-x.wmi
%{_datadir}/doc/%{name}/plugins.binary/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/plugins.conky/conky.audacious.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.conf
%{_datadir}/doc/%{name}/plugins.conky/conky.date.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.diskmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.entropy.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.filesystem1.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.forecast.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.memory.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.mixer.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.moc.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.mpd.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.multi-system1.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.multi-system2.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.multi-time.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.netmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.patch
%{_datadir}/doc/%{name}/plugins.conky/conky.swap.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.sysmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.timezone.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.topmem.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.toptime.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.top.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.uptime.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.weather.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.wireless.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.wrapper-sun-moon-tz.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.wrapper-weather.wmi
%{_datadir}/doc/%{name}/plugins.conky/conky.xmms2.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.1st.plugins.conky
%{_datadir}/doc/%{name}/plugins.conky/README.2nd.plugins.conky
%{_datadir}/doc/%{name}/plugins.conky/README.conky.date.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.diskmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.filesystem.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.forecast.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.mixer.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.moc.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.mpd.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.netmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.sysmon.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.timezone.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.top.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.uptime.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.weather.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.wireless.wmi
%{_datadir}/doc/%{name}/plugins.conky/README.conky.xmms2.wmi
%{_datadir}/doc/%{name}/plugins.conky/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/Plugins-HOWTO
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
%{_datadir}/doc/%{name}/plugins.offline/forecast.new-york.wmi
%{_datadir}/doc/%{name}/plugins.offline/forecast.sydney.wmi
%{_datadir}/doc/%{name}/plugins.offline/forecast.wroclaw.wmi
%{_datadir}/doc/%{name}/plugins.offline/freecode.wmi
%{_datadir}/doc/%{name}/plugins.offline/kernel-2.4.wmi
%{_datadir}/doc/%{name}/plugins.offline/kernel-2.6.wmi
%{_datadir}/doc/%{name}/plugins.offline/kernel-3.x.wmi
%{_datadir}/doc/%{name}/plugins.offline/kommersant.wmi
%{_datadir}/doc/%{name}/plugins.offline/linuxquestions-slackware.wmi
%{_datadir}/doc/%{name}/plugins.offline/nasdaq.wmi
%{_datadir}/doc/%{name}/plugins.offline/online
%{_datadir}/doc/%{name}/plugins.offline/pitchfork.wmi
%{_datadir}/doc/%{name}/plugins.offline/README.1st.plugins.offline
%{_datadir}/doc/%{name}/plugins.offline/README.forecast.xxx.wmi
%{_datadir}/doc/%{name}/plugins.offline/README.weather.wmi
%{_datadir}/doc/%{name}/plugins.offline/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/plugins.offline/slackbuilds.wmi
%{_datadir}/doc/%{name}/plugins.offline/slackware-patches.wmi
%{_datadir}/doc/%{name}/plugins.offline/slashdot.wmi
%{_datadir}/doc/%{name}/plugins.offline/spiegel.wmi
%{_datadir}/doc/%{name}/plugins.offline/tvn24.wmi
%{_datadir}/doc/%{name}/plugins.offline/twitter.wmi
%{_datadir}/doc/%{name}/plugins.offline/weather.wmi
%{_datadir}/doc/%{name}/plugins.offline/wrapper-currencies-pl.wmi
%{_datadir}/doc/%{name}/plugins.offline/wrapper-internet-allinone.wmi
%{_datadir}/doc/%{name}/plugins.offline/wrapper-weather.wmi
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
%{_datadir}/doc/%{name}/plugins.online/forecast.new-york.wmi
%{_datadir}/doc/%{name}/plugins.online/forecast.sydney.wmi
%{_datadir}/doc/%{name}/plugins.online/forecast.wroclaw.wmi
%{_datadir}/doc/%{name}/plugins.online/freecode.wmi
%{_datadir}/doc/%{name}/plugins.online/kernel-2.4.wmi
%{_datadir}/doc/%{name}/plugins.online/kernel-2.6.wmi
%{_datadir}/doc/%{name}/plugins.online/kernel-3.x.wmi
%{_datadir}/doc/%{name}/plugins.online/kommersant.wmi
%{_datadir}/doc/%{name}/plugins.online/linuxquestions-slackware.wmi
%{_datadir}/doc/%{name}/plugins.online/nasdaq.wmi
%{_datadir}/doc/%{name}/plugins.online/pitchfork.wmi
%{_datadir}/doc/%{name}/plugins.online/README.1st.plugins.online
%{_datadir}/doc/%{name}/plugins.online/README.forecast.xxx.wmi
%{_datadir}/doc/%{name}/plugins.online/README.weather.wmi
%{_datadir}/doc/%{name}/plugins.online/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/plugins.online/slackbuilds.wmi
%{_datadir}/doc/%{name}/plugins.online/slackware-patches.wmi
%{_datadir}/doc/%{name}/plugins.online/slashdot.wmi
%{_datadir}/doc/%{name}/plugins.online/spiegel.wmi
%{_datadir}/doc/%{name}/plugins.online/tvn24.wmi
%{_datadir}/doc/%{name}/plugins.online/twitter.wmi
%{_datadir}/doc/%{name}/plugins.online/weather.wmi
%{_datadir}/doc/%{name}/plugins.online/wrapper-currencies-pl.wmi
%{_datadir}/doc/%{name}/plugins.online/wrapper-internet-allinone.wmi
%{_datadir}/doc/%{name}/plugins.online/wrapper-weather.wmi
%{_datadir}/doc/%{name}/plugins.online/wyborcza.wmi
%{_datadir}/doc/%{name}/plugins.system/alarm
%{_datadir}/doc/%{name}/plugins.system/alarm.cfg
%{_datadir}/doc/%{name}/plugins.system/alarm.wmi
%{_datadir}/doc/%{name}/plugins.system/biff.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-horizontal.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-04.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-05.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-06.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-07.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-08.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-09.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-10.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-11.wmi
%{_datadir}/doc/%{name}/plugins.system/binclock-vertical-12.wmi
%{_datadir}/doc/%{name}/plugins.system/cpumon.wmi
%{_datadir}/doc/%{name}/plugins.system/date-pl
%{_datadir}/doc/%{name}/plugins.system/date-pl.cfg
%{_datadir}/doc/%{name}/plugins.system/date-pl.wmi
%{_datadir}/doc/%{name}/plugins.system/date-us
%{_datadir}/doc/%{name}/plugins.system/date-us.cfg
%{_datadir}/doc/%{name}/plugins.system/date-us.wmi
%{_datadir}/doc/%{name}/plugins.system/date.wmi
%{_datadir}/doc/%{name}/plugins.system/days
%{_datadir}/doc/%{name}/plugins.system/days.cfg
%{_datadir}/doc/%{name}/plugins.system/days.wmi
%{_datadir}/doc/%{name}/plugins.system/df.wmi
%{_datadir}/doc/%{name}/plugins.system/hexclock.wmi
%{_datadir}/doc/%{name}/plugins.system/ip.wmi
%{_datadir}/doc/%{name}/plugins.system/julian-date.wmi
%{_datadir}/doc/%{name}/plugins.system/memory.wmi
%{_datadir}/doc/%{name}/plugins.system/netmon.wmi
%{_datadir}/doc/%{name}/plugins.system/pinboard
%{_datadir}/doc/%{name}/plugins.system/pinboard.wmi
%{_datadir}/doc/%{name}/plugins.system/ps.wmi
%{_datadir}/doc/%{name}/plugins.system/README.1st.plugins.system
%{_datadir}/doc/%{name}/plugins.system/README.alarm.wmi
%{_datadir}/doc/%{name}/plugins.system/README.biff.wmi
%{_datadir}/doc/%{name}/plugins.system/README.binclock-vertical-x.wmi
%{_datadir}/doc/%{name}/plugins.system/README.date.wmi
%{_datadir}/doc/%{name}/plugins.system/README.date-xx.wmi
%{_datadir}/doc/%{name}/plugins.system/README.days.wmi
%{_datadir}/doc/%{name}/plugins.system/README.netmon.wmi
%{_datadir}/doc/%{name}/plugins.system/README.stopwatch.wmi
%{_datadir}/doc/%{name}/plugins.system/README.sun-moon.wmi
%{_datadir}/doc/%{name}/plugins.system/README.sysmon.wmi
%{_datadir}/doc/%{name}/plugins.system/README.thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.system/README.timer.wmi
%{_datadir}/doc/%{name}/plugins.system/README.timezone.wmi
%{_datadir}/doc/%{name}/plugins.system/README.traffic.wmi
%{_datadir}/doc/%{name}/plugins.system/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/plugins.system/solunar.patch
%{_datadir}/doc/%{name}/plugins.system/stopwatch
%{_datadir}/doc/%{name}/plugins.system/stopwatch.cfg
%{_datadir}/doc/%{name}/plugins.system/stopwatch.wmi
%{_datadir}/doc/%{name}/plugins.system/sun-moon.wmi
%{_datadir}/doc/%{name}/plugins.system/sysmon.wmi
%{_datadir}/doc/%{name}/plugins.system/thinkpad.wmi
%{_datadir}/doc/%{name}/plugins.system/timer
%{_datadir}/doc/%{name}/plugins.system/timer.cfg
%{_datadir}/doc/%{name}/plugins.system/timer.wmi
%{_datadir}/doc/%{name}/plugins.system/timezone
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.default
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.GMT.CODES
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.GMT.offsets
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.Reg-Cty.ISOs
%{_datadir}/doc/%{name}/plugins.system/timezone.cfg.Reg-Cty.zones
%{_datadir}/doc/%{name}/plugins.system/timezone.wmi
%{_datadir}/doc/%{name}/plugins.system/top.wmi
%{_datadir}/doc/%{name}/plugins.system/traffic.wmi
%{_datadir}/doc/%{name}/plugins.system/uptime.wmi
%{_datadir}/doc/%{name}/plugins.system/wrapper-date-pinboard.wmi
%{_datadir}/doc/%{name}/plugins.system/wrapper-date-tz.wmi
%{_datadir}/doc/%{name}/plugins.system/wrapper-df.wmi
%{_datadir}/doc/%{name}/plugins.system/wrapper-sun-moon-tz.wmi
%{_datadir}/doc/%{name}/README
%{_datadir}/doc/%{name}/README.1st
%{_datadir}/doc/%{name}/README.benchmarks
%{_datadir}/doc/%{name}/README.colors
%{_datadir}/doc/%{name}/README.CPU.usage
%{_datadir}/doc/%{name}/README.multi+wrapper
%{_datadir}/doc/%{name}/samples/a-1050-line-plugin.wmi
%{_datadir}/doc/%{name}/samples/a-1913-letter-plugin.wmi
%{_datadir}/doc/%{name}/samples/binclock-vertical-13.wmi
%{_datadir}/doc/%{name}/samples/full-utf8.html
%{_datadir}/doc/%{name}/samples/full-utf8-iso1.wmi
%{_datadir}/doc/%{name}/samples/full-utf8-iso2.wmi
%{_datadir}/doc/%{name}/samples/full-utf8-iso5.wmi
%{_datadir}/doc/%{name}/samples/html.html
%{_datadir}/doc/%{name}/samples/html-iso1.wmi
%{_datadir}/doc/%{name}/samples/html-iso2.wmi
%{_datadir}/doc/%{name}/samples/html-iso5.wmi
%{_datadir}/doc/%{name}/samples/quick-koi8r-dummy.wmi
%{_datadir}/doc/%{name}/samples/quick-koi8r.html
%{_datadir}/doc/%{name}/samples/quick-koi8r-iso5.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8-dummy.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8.html
%{_datadir}/doc/%{name}/samples/quick-utf8-iso1.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8-iso2.wmi
%{_datadir}/doc/%{name}/samples/quick-utf8-iso5.wmi
%{_datadir}/doc/%{name}/samples/README.samples
%{_datadir}/doc/%{name}/samples/run-all-wminfo-plugins
%{_datadir}/doc/%{name}/samples/test-00-50.wmi
%{_datadir}/doc/%{name}/samples/test-50-00.wmi
%{_datadir}/doc/%{name}/samples/test.html
%{_datadir}/doc/%{name}/THANKS
%{_datadir}/doc/%{name}/TODO
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Jan 09 2013 J. Krebs <rpm_speedy@yahoo.com> - 4.0.0-1
- New version.

* Sat Jul 07 2012 J. Krebs <rpm_speedy@yahoo.com> - 3.0.0-1
- New version.

* Thu Jan 26 2012 J. Krebs <rpm_speedy@yahoo.com> - 2.5.2-1
- Initial build.
