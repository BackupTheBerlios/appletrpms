RPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/i586.rpm/')
SRPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/src.rpm/')
RPMDIR=rpmdir
SRPMDIR=srpmdir

BUILD=BUILD
SOURCES=SOURCES
SPECS=SPECS
TEST=asapm.rpm

include include/*inc

all: 
	$(foreach app, $(APPLET_LIST), \
		make $(app).rpm ) \
		&& /bin/true

%.done: %.rpm

%.rpm:
	echo $(patsubst %.rpm,%,$@)
	rm -f $(SOURCES)/$($(patsubst %.rpm,%,$@)_TAR)
	wget -O $(SOURCES)/$($(patsubst %.rpm,%,$@)_TAR) $($(patsubst %.rpm,%,$@)_URL)
	rpm --define='_topdir $(PWD)' -bs $(SPECS)/$($(patsubst %.rpm,%,$@)_NAME).spec
	rpm --define='_topdir $(PWD)' -ba $(SPECS)/$($(patsubst %.rpm,%,$@)_NAME).spec
	touch $(patsubst %.rpm,%.done,$@)

.SUFFIXES: done rpm

.PHONY: clean $(patsubst %,%.done,$(APPLET_LIST))