BUILD=BUILD
SOURCES=SOURCES
SPECS=SPECS
RPMS=RPMS

include include/*inc

all: download build meta_rpm

build: download
	./buildme all

download:
	./buildme download

meta_rpm:
	./buildme meta_rpm

$(APPLET_LIST):
	./buildme $@

mdk-i586: 
	cd $(RPMS)/i586/ && genhdlist .

fc3-i386: 
	cd $(RPMS)/i386/ && createrepo .

#dist: all mdk-i586
	

publish: all meta_rpm
	./publish

clean:
	./buildme clean
	find $(BUILD) -name \* | grep -v keepme | xargs rm -f 
	find . -name \*~ | xargs rm -f


