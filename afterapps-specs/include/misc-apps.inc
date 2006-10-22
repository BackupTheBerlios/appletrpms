# -*- makefile -*-
#
# misc applets that didn't seem to be specific to any wm

#this is the first of three tarballs needed to build ascd-themes
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

LIBDOCKAPP_NAME=libdockapp
LIBDOCKAPP_VERSION=0.6.1
LIBDOCKAPP_TAR=$(LIBDOCKAPP_NAME)-$(LIBDOCKAPP_VERSION).tar.bz2
LIBDOCKAPP_URL=http://solfertje.student.utwente.nl/~dalroi/$(LIBDOCKAPP_NAME)/files/$(LIBDOCKAPP_TAR)

APPLET_LIST += LIBDOCKAPP

LIBICAL_NAME=libical
LIBICAL_VERSION=0.24.RC4
LIBICAL_TAR=$(LIBICAL_NAME)-$(LIBICAL_VERSION).tar.gz
LIBICAL_URL=http://easynews.dl.sourceforge.net/sourceforge/freeassociation/$(LIBICAL_TAR)

APPLET_LIST += LIBICAL

#this is the the source file used to build libwraster
LIBWRASTER_NAME=libwraster
LIBWRASTER_VERSION=0.80.2
LIBWRASTER_TAR=WindowMaker-$(LIBWRASTER_VERSION).tar.gz
LIBWRASTER_URL=http://open-systems.ufl.edu/mirrors/gentoo/distfiles/$(LIBWRASTER_TAR)

#APPLET_LIST += LIBWRASTER

MIXER.APP_NAME=Mixer.app
MIXER.APP_VERSION=1.8.0
MIXER.APP_TAR=$(MIXER.APP_NAME)-$(MIXER.APP_VERSION).tar.gz
MIXER.APP_URL=http://www.fukt.bth.se/~per/mixer/$(MIXER.APP_TAR)

APPLET_LIST += MIXER.APP

SALMON_NAME=salmon
SALMON_VERSION=1.2.2
SALMON_TAR=$(SALMON_NAME)-$(SALMON_VERSION).tar.gz
SALMON_URL=http://tigr.net/afterstep/download/salmon/$(SALMON_TAR)

APPLET_LIST += SALMON

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
