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
ASCD-THEMES_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(ASCD-THEMES_TAR)

APPLET_LIST += ASCD-THEMES

#this is the second of three tarballs needed to build ascd-themes
DWING_NOSPEC=YES
DWING_NAME=dwing
DWING_VERSION=1.10
DWING_TAR=$(DWING_NAME).tgz
DWING_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(DWING_TAR)

#APPLET_LIST += DWING

#this is the third of three tarballs needed to build ascd-themes
LCD_NOSPEC=YES
LCD_NAME=lcd
LCD_VERSION=1.10
LCD_TAR=$(LCD_NAME).tar.gz
LCD_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(LCD_TAR)

#APPLET_LIST += LCD

AVFS_NAME=avfs
AVFS_VERSION=1.0.0
AVFS_TAR=$(AVFS_NAME)-$(AVFS_VERSION).tar.gz
AVFS_URL=http://downloads.sourceforge.net/project/avf/$(AVFS_NAME)/$(AVFS_VERSION)/$(AVFS_TAR)

APPLET_LIST += AVFS

CALCOO_NAME=calcoo
CALCOO_VERSION=1.3.18
CALCOO_TAR=$(CALCOO_NAME)-$(CALCOO_VERSION).tar.gz
CALCOO_URL=http://downloads.sourceforge.net/project/$(CALCOO_NAME)/$(CALCOO_NAME)/$(CALCOO_TAR)

APPLET_LIST += CALCOO

#eina 0.10.0+ needs gtk3-3.0.0+, only available under Fedora 15+
EINA_NAME=eina
EINA_VERSION=0.10.0
EINA_TAR=$(EINA_NAME)-$(EINA_VERSION).tar.gz
EINA_URL=http://launchpad.net/eina/trunk/$(EINA_VERSION)/+download/$(EINA_TAR)

APPLET_LIST += EINA

FOTOXX_NAME=fotoxx
FOTOXX_VERSION=11.08
FOTOXX_TAR=$(FOTOXX_NAME)-$(FOTOXX_VERSION).tar.gz
FOTOXX_URL=http://kornelix.squarespace.com/storage/downloads/$(FOTOXX_TAR)

APPLET_LIST += FOTOXX

# Included in Fedora 15 Repository
#LIBDOCKAPP_NAME=libdockapp
#LIBDOCKAPP_VERSION=0.6.2
#LIBDOCKAPP_TAR=$(LIBDOCKAPP_NAME)-$(LIBDOCKAPP_VERSION).tar.bz2
#LIBDOCKAPP_URL=http://solfertje.student.utwente.nl/~dalroi/$(LIBDOCKAPP_NAME)/files/$(LIBDOCKAPP_TAR)

#APPLET_LIST += LIBDOCKAPP

# Included in Fedora 15 Repository
#LIBICAL_NAME=libical
#LIBICAL_VERSION=0.43
#LIBICAL_TAR=$(LIBICAL_NAME)-$(LIBICAL_VERSION).tar.gz
#LIBICAL_URL=http://easynews.dl.sourceforge.net/sourceforge/freeassociation/$(LIBICAL_TAR)
#
#APPLET_LIST += LIBICAL

# Substitute WindowMaker
#this is the the source file used to build libwraster
#LIBWRASTER_NAME=libwraster
#LIBWRASTER_VERSION=0.80.2
#LIBWRASTER_TAR=WindowMaker-$(LIBWRASTER_VERSION).tar.gz
#LIBWRASTER_URL=http://windowmaker.info/pub/source/archive/$(LIBWRASTER_TAR)

#APPLET_LIST += LIBWRASTER

MEDIT_NAME=medit
MEDIT_VERSION=1.0.3
MEDIT_TAR=$(MEDIT_NAME)-$(MEDIT_VERSION).tar.bz2
MEDIT_URL=http://sourceforge.net/projects/mooedit/files/$(MEDIT_NAME)/$(MEDIT_VERSION)/$(MEDIT_TAR)

APPLET_LIST += MEDIT

MINED_NAME=mined
MINED_VERSION=2011.17
MINED_TAR=$(MINED_NAME)-$(MINED_VERSION).tar.gz
MINED_URL=http://towo.net/mined/download/$(MINED_TAR)

APPLET_LIST += MINED

MIXER.APP_NAME=Mixer.app
MIXER.APP_VERSION=1.8.0
MIXER.APP_TAR=$(MIXER.APP_NAME)-$(MIXER.APP_VERSION).tar.gz
MIXER.APP_URL=http://www.fukt.bsnet.se/~per/mixer/$(MIXER.APP_TAR)

APPLET_LIST += MIXER.APP

# Included in Fedora's Repository
#PARCELLITE_NAME=parcellite
#PARCELLITE_VERSION=0.9.1
#PARCELLITE_TAR=$(PARCELLITE_NAME)-$(PARCELLITE_VERSION).tar.gz
#PARCELLITE_URL=http://downloads.sourceforge.net/project/$(PARCELLITE_NAME)/$(PARCELLITE_NAME)/$(PARCELLITE_NAME)-$(PARCELLITE_VERSION)/$(PARCELLITE_TAR)
#
#APPLET_LIST += PARCELLITE

SALMON_NAME=salmon
SALMON_VERSION=1.2.2
SALMON_TAR=$(SALMON_NAME)-$(SALMON_VERSION).tar.gz
SALMON_URL=http://tigr.net/afterstep/download/salmon/$(SALMON_TAR)

APPLET_LIST += SALMON

STALONETRAY_NAME=stalonetray
STALONETRAY_VERSION=0.8.1
STALONETRAY_TAR=$(STALONETRAY_NAME)-$(STALONETRAY_VERSION).tar.gz
STALONETRAY_URL=http://downloads.sourceforge.net/project/$(STALONETRAY_NAME)/$(STALONETRAY_NAME)/$(STALONETRAY_TAR)

APPLET_LIST += STALONETRAY

TEMPERATURE.APP_NAME=Temperature.app
TEMPERATURE.APP_VERSION=1.4
TEMPERATURE.APP_TAR=$(TEMPERATURE.APP_NAME)-$(TEMPERATURE.APP_VERSION).tar.gz
TEMPERATURE.APP_URL=http://www.fukt.bsnet.se/~per/temperature/$(TEMPERATURE.APP_TAR)

APPLET_LIST += TEMPERATURE.APP

TRAYER_NAME=trayer
TRAYER_VERSION=1.1.2
TRAYER_TAR=sargon-trayer-srg-$(TRAYER_NAME)_$(TRAYER_VERSION)-1-g77e2eb2.tar.gz
TRAYER_URL=https://github.com/sargon/trayer-srg/tarball/master/$(TRAYER_TAR)
APPLET_LIST += TRAYER

WORKER_NAME=worker
WORKER_VERSION=2.18.0
WORKER_TAR=$(WORKER_NAME)-$(WORKER_VERSION).tar.gz
WORKER_URL=http://www.boomerangsworld.de/worker/downloads/$(WORKER_TAR)

APPLET_LIST += WORKER

# Let's kill this outdated documentation.  Rely for online info
#WORKER-DOC_NOSPEC=YES
#WORKER-DOC_NAME=worker
#WORKER-DOC_VERSION=2.10.0.2
#WORKER-DOC_TAR=$(WORKER-DOC_NAME)-$(WORKER-DOC_VERSION)-doc.tar.bz2
#WORKER-DOC_URL=http://www.boomerangsworld.de/worker/downloads/$(WORKER-DOC_TAR)

#APPLET_LIST += WORKER-DOC

XSENSORS_NAME=xsensors
XSENSORS_VERSION=0.70
XSENSORS_TAR=$(XSENSORS_NAME)-$(XSENSORS_VERSION).tar.gz
XSENSORS_URL=http://www.linuxhardware.org/$(XSENSORS_NAME)/$(XSENSORS_TAR)

APPLET_LIST += XSENSORS

YUDIT_NAME=yudit
YUDIT_VERSION=2.9.2
YUDIT_TAR=$(YUDIT_NAME)-$(YUDIT_VERSION).tar.gz
YUDIT_URL=http://yudit.org/download/$(YUDIT_TAR)

APPLET_LIST += YUDIT
