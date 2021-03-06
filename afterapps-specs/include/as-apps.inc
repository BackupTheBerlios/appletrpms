# -*- makefile -*-

# APM and SMP don't play nicely
# AfterStep apm applet
#ASAPM_NAME=asapm
#ASAPM_VERSION=3.1
#ASAPM_TAR=$(ASAPM_NAME)-$(ASAPM_VERSION).tar.gz
#ASAPM_URL=http://tigr.net/afterstep/download/asapm/$(ASAPM_TAR)

#APPLET_LIST += ASAPM

# Seems to require OSS, OSS and pulse don't seem to work together
# This version of ascd includes the source to libworkman
#ASCD_NAME=ascd
#ASCD_VERSION=0.13.2
#ASCD_TAR=$(ASCD_NAME)-$(ASCD_VERSION).tar.gz
#ASCD_URL=http://tigr.net/afterstep/download/$(ASCD_NAME)/$(ASCD_TAR)

#APPLET_LIST += ASCD

ASCLOCK_NAME=asclock
ASCLOCK_VERSION=2.0.12
ASCLOCK_TAR=$(ASCLOCK_NAME)-$(ASCLOCK_VERSION).tar.gz
ASCLOCK_URL=http://tigr.net/afterstep/download/$(ASCLOCK_NAME)/$(ASCLOCK_TAR)

APPLET_LIST += ASCLOCK

ASCPU_NAME=ascpu
ASCPU_VERSION=1.11
ASCPU_TAR=$(ASCPU_NAME)-$(ASCPU_VERSION).tar.gz
ASCPU_URL=http://tigr.net/afterstep/download/$(ASCPU_NAME)/$(ASCPU_TAR)

APPLET_LIST += ASCPU

ASFSMLITE_NAME=asfsm_lite
ASFSMLITE_VERSION=1.0.0
ASFSMLITE_TAR=$(ASFSMLITE_NAME)-$(ASFSMLITE_VERSION).tar.gz
ASFSMLITE_URL=http://tigr.net/afterstep/download/$(ASFSMLITE_NAME)/$(ASFSMLITE_TAR)

APPLET_LIST += ASFSMLITE

ASLOAD_NAME=asload
ASLOAD_VERSION=0.9.4
ASLOAD_TAR=$(ASLOAD_NAME)-$(ASLOAD_VERSION).tar.gz
ASLOAD_URL=http://tigr.net/afterstep/download/$(ASLOAD_NAME)/$(ASLOAD_TAR)

APPLET_LIST += ASLOAD

ASMAIL_NAME=asmail
ASMAIL_VERSION=2.1
ASMAIL_TAR=$(ASMAIL_NAME)-$(ASMAIL_VERSION).tar.gz
ASMAIL_URL=http://tigr.net/afterstep/download/$(ASMAIL_NAME)/$(ASMAIL_TAR)

APPLET_LIST += ASMAIL

ASMEM_NAME=asmem
ASMEM_VERSION=1.12
ASMEM_TAR=$(ASMEM_NAME)-$(ASMEM_VERSION).tar.gz
ASMEM_URL=http://tigr.net/afterstep/download/$(ASMEM_NAME)/$(ASMEM_TAR)

APPLET_LIST += ASMEM

#OSS and pulse don't seem to work together
#ASMIX_NAME=asmix
#ASMIX_VERSION=1.5
#ASMIX_TAR=$(ASMIX_NAME)-$(ASMIX_VERSION).tar.gz
#ASMIX_URL=http://tigr.net/afterstep/download/$(ASMIX_NAME)/$(ASMIX_TAR)

#APPLET_LIST += ASMIX

#OSS and pulse don't seem to work together
#ASMIXER_NAME=asmixer
#ASMIXER_VERSION=0.5
#ASMIXER_TAR=$(ASMIXER_NAME)-$(ASMIXER_VERSION).tar.gz
#ASMIXER_URL=http://tigr.net/afterstep/download/$(ASMIXER_NAME)/$(ASMIXER_TAR)

#APPLET_LIST += ASMIXER

ASMODEM_NAME=asmodem

ASMODEM_VERSION=0.6
ASMODEM_TAR=$(ASMODEM_NAME)-$(ASMODEM_VERSION)-1.tar.gz
ASMODEM_URL=http://tigr.net/afterstep/download/$(ASMODEM_NAME)/$(ASMODEM_TAR)

APPLET_LIST += ASMODEM

# the "newer" version at http://rio.vg/asmon/, appears to be by one of the original
# author(s). We'll use that rather than the one from tigr.net.
ASMON_NAME=asmon
ASMON_VERSION=0.71
ASMON_TAR=$(ASMON_NAME)-$(ASMON_VERSION).tar.bz2
ASMON_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(ASMON_TAR)

APPLET_LIST += ASMON

ASMOUNT_NAME=asmount
ASMOUNT_VERSION=1.0.0
ASMOUNT_TAR=$(ASMOUNT_NAME)-$(ASMOUNT_VERSION).tar.gz
ASMOUNT_URL=http://tigr.net/afterstep/download/$(ASMOUNT_NAME)/$(ASMOUNT_TAR)

APPLET_LIST += ASMOUNT

ASPOSTIT_NAME=aspostit
ASPOSTIT_VERSION=1.3
ASPOSTIT_TAR=$(ASPOSTIT_NAME)-$(ASPOSTIT_VERSION).tar.gz
ASPOSTIT_URL=http://tigr.net/afterstep/download/$(ASPOSTIT_NAME)/$(ASPOSTIT_TAR)

APPLET_LIST += ASPOSTIT

ASTIME_NAME=astime
ASTIME_VERSION=2.8
ASTIME_TAR=$(ASTIME_NAME)-$(ASTIME_VERSION).tar.gz
ASTIME_URL=http://tigr.net/afterstep/download/$(ASTIME_NAME)/$(ASTIME_TAR)

APPLET_LIST += ASTIME

ASWVDIAL_NAME=aswvdial
ASWVDIAL_VERSION=1.7
ASWVDIAL_TAR=$(ASWVDIAL_NAME)-$(ASWVDIAL_VERSION).tar.bz2
ASWVDIAL_URL=ftp://ftp.afterstep.org/stable/rpms/misc-tarballs/$(ASWVDIAL_TAR)

APPLET_LIST += ASWVDIAL

