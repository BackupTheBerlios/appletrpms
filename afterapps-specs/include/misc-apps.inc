# -*- makefile -*-
#
# misc applets that didn't seem to be specific to any wm

#this is the first of three tarballs needed to build Propaganda
PROPAGANDA_NAME=Propaganda
PROPAGANDA_VERSION=1
PROPAGANDA_TAR=$(PROPAGANDA_NAME)-EVERYTHING.tar.bz2
PROPAGANDA_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(PROPAGANDA_TAR)

APPLET_LIST += PROPAGANDA

#this is the first of three tarballs needed to build Propaganda
PROPAGANDA-VOL13_NOSPEC=YES
PROPAGANDA-VOL13_NAME=Propaganda-Vol13
PROPAGANDA-VOL13_VERSION=13
PROPAGANDA-VOL13_TAR=$(PROPAGANDA-VOL13_NAME).tar.bz2
PROPAGANDA-VOL13_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(PROPAGANDA-VOL13_TAR)

APPLET_LIST += PROPAGANDA-VOL13

#this is the first of three tarballs needed to build Propaganda
PROPAGANDA-VOL14_NOSPEC=YES
PROPAGANDA-VOL14_NAME=Propaganda-Vol14
PROPAGANDA-VOL14_VERSION=14
PROPAGANDA-VOL14_TAR=$(PROPAGANDA-VOL14_NAME).tar.bz2
PROPAGANDA-VOL14_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(PROPAGANDA-VOL14_TAR)

APPLET_LIST += PROPAGANDA-VOL14

#this is the first of three tarballs needed to build ascd-themes
ASCD-THEMES_NOSPEC=YES
ASCD-THEMES_NAME=ascd-themes
ASCD-THEMES_VERSION=1.13
ASCD-THEMES_TAR=ascd-0.13pr6-themes.tgz
ASCD-THEMES_URL=http://worldserver.oleane.com/rsn/Archives/$(ASCD-THEMES_TAR)

APPLET_LIST += ASCD-THEMES

#this is the second of three tarballs needed to build ascd-themes
DWING_NOSPEC=YES
DWING_NAME=dwing
DWING_VERSION=1.10
DWING_TAR=$(DWING_NAME).tgz
DWING_URL=http://worldserver.oleane.com/rsn/Archives/$(DWING_TAR)

#APPLET_LIST += DWING

#this is the third of three tarballs needed to build ascd-themes
LCD_NOSPEC=YES
LCD_NAME=lcd
LCD_VERSION=1.10
LCD_TAR=$(LCD_NAME).tar.gz
LCD_URL=http://worldserver.oleane.com/rsn/Archives/$(LCD_TAR)

#APPLET_LIST += LCD

AVFS_NAME=avfs
AVFS_VERSION=0.9.8
AVFS_TAR=$(AVFS_NAME)-$(AVFS_VERSION).tar.gz
AVFS_URL=http://easynews.dl.sourceforge.net/sourceforge/avf/$(AVFS_TAR)

APPLET_LIST += AVFS

CALCOO_NAME=calcoo
CALCOO_VERSION=1.3.18
CALCOO_TAR=$(CALCOO_NAME)-$(CALCOO_VERSION).tar.gz
CALCOO_URL=http://internap.dl.sourceforge.net/sourceforge/$(CALCOO_NAME)/$(CALCOO_TAR)

APPLET_LIST += CALCOO

FOTOXX_NAME=fotoxx
FOTOXX_VERSION=4.7
FOTOXX_TAR=$(FOTOXX_NAME)-$(FOTOXX_VERSION).tar.gz
FOTOXX_URL=http://kornelix.squarespace.com/storage/programs/$(FOTOXX_NAME)/$(FOTOXX_TAR)

APPLET_LIST += FOTOXX

LIBDOCKAPP_NAME=libdockapp
LIBDOCKAPP_VERSION=0.6.1
LIBDOCKAPP_TAR=$(LIBDOCKAPP_NAME)-$(LIBDOCKAPP_VERSION).tar.bz2
LIBDOCKAPP_URL=http://solfertje.student.utwente.nl/~dalroi/$(LIBDOCKAPP_NAME)/files/$(LIBDOCKAPP_TAR)

APPLET_LIST += LIBDOCKAPP

LIBICAL_NAME=libical
LIBICAL_VERSION=0.31
LIBICAL_TAR=$(LIBICAL_NAME)-$(LIBICAL_VERSION).tar.gz
LIBICAL_URL=http://easynews.dl.sourceforge.net/sourceforge/freeassociation/$(LIBICAL_TAR)

APPLET_LIST += LIBICAL

#this is the the source file used to build libwraster
LIBWRASTER_NAME=libwraster
LIBWRASTER_VERSION=0.80.2
LIBWRASTER_TAR=WindowMaker-$(LIBWRASTER_VERSION).tar.gz
LIBWRASTER_URL=http://www.windowmaker.info/pub/source/release/archive/$(LIBWRASTER_TAR)

#APPLET_LIST += LIBWRASTER

MEDIT_NAME=medit
MEDIT_VERSION=0.9.3
MEDIT_TAR=$(MEDIT_NAME)-$(MEDIT_VERSION).tar.bz2
MEDIT_URL=http://easynews.dl.sourceforge.net/sourceforge/mooedit/$(MEDIT_TAR)

APPLET_LIST += MEDIT

MINED_NAME=mined
MINED_VERSION=2000.14
MINED_TAR=$(MINED_NAME)-$(MINED_VERSION).tar.gz
MINED_URL=http://towo.net/$(MINED_NAME)/$(MINED_TAR)

APPLET_LIST += MINED

MIXER.APP_NAME=Mixer.app
MIXER.APP_VERSION=1.8.0
MIXER.APP_TAR=$(MIXER.APP_NAME)-$(MIXER.APP_VERSION).tar.gz
MIXER.APP_URL=http://www.fukt.bth.se/~per/mixer/$(MIXER.APP_TAR)

APPLET_LIST += MIXER.APP

PARCELLITE_NAME=parcellite
PARCELLITE_VERSION=0.7
PARCELLITE_TAR=$(PARCELLITE_NAME)-$(PARCELLITE_VERSION).tar.gz
PARCELLITE_URL=http://xyhthyx.googlecode.com/files/$(PARCELLITE_TAR)

APPLET_LIST += PARCELLITE

SALMON_NAME=salmon
SALMON_VERSION=1.2.2
SALMON_TAR=$(SALMON_NAME)-$(SALMON_VERSION).tar.gz
SALMON_URL=http://tigr.net/afterstep/download/salmon/$(SALMON_TAR)

APPLET_LIST += SALMON

STALONETRAY_NAME=stalonetray
STALONETRAY_VERSION=0.7.6
STALONETRAY_TAR=$(STALONETRAY_NAME)-$(STALONETRAY_VERSION).tar.gz
STALONETRAY_URL=http://easynews.dl.sourceforge.net/sourceforge/$(STALONETRAY_NAME)/$(STALONETRAY_TAR)

APPLET_LIST += STALONETRAY

TEMPERATURE.APP_NAME=Temperature.app
TEMPERATURE.APP_VERSION=1.4
TEMPERATURE.APP_TAR=$(TEMPERATURE.APP_NAME)-$(TEMPERATURE.APP_VERSION).tar.gz
TEMPERATURE.APP_URL=http://www.fukt.bth.se/~per/temperature/$(TEMPERATURE.APP_TAR)

APPLET_LIST += TEMPERATURE.APP

TRAYER_NAME=trayer
TRAYER_VERSION=1.0
TRAYER_TAR=$(TRAYER_NAME)-$(TRAYER_VERSION).tar.gz
TRAYER_URL=http://download.gna.org/fvwm-crystal/$(TRAYER_NAME)/$(TRAYER_VERSION)/$(TRAYER_TAR)

APPLET_LIST += TRAYER

WORKER_NAME=worker
WORKER_VERSION=2.16.3
WORKER_TAR=$(WORKER_NAME)-$(WORKER_VERSION).tar.gz
WORKER_URL=http://www.boomerangsworld.de/worker/downloads/$(WORKER_TAR)

APPLET_LIST += WORKER

WORKER-DOC_NOSPEC=YES
WORKER-DOC_NAME=worker
WORKER-DOC_VERSION=2.10.0.2
WORKER-DOC_TAR=$(WORKER-DOC_NAME)-$(WORKER-DOC_VERSION)-doc.tar.bz2
WORKER-DOC_URL=http://www.boomerangsworld.de/worker/downloads/$(WORKER-DOC_TAR)

APPLET_LIST += WORKER-DOC

YUDIT_NAME=yudit
YUDIT_VERSION=2.9.0
YUDIT_TAR=$(YUDIT_NAME)-$(YUDIT_VERSION).tar.gz
YUDIT_URL=http://yudit.org/download/$(YUDIT_TAR)

APPLET_LIST += YUDIT
