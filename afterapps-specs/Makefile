RPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/i586.rpm/')
SRPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/src.rpm/')
RPMDIR=rpmdir
SRPMDIR=srpmdir

BUILD=BUILD
SOURCES=SOURCES
SPECS=SPECS
TEST=asapm.rpm

include include/*inc

all: download build

build: download
	./buildme all

download:
	./buildme download

$(APPLET_LIST):
	./buildme $@

clean:
	./buildme clean
	find $(BUILD) . -name \* | grep -v keepme | xargs rm -f 
	find . -name \*~ | xargs rm -f



