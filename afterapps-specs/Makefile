RPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/i586.rpm/')
SRPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/src.rpm/')
BUILDDIR=build

all: $(BUILDDIR) rpms srpms

rpms: $(RPMS) 

srpms: $(SRPMS)

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

%.i586.rpm: %.spec
	cp -a $(shell rpm -bb $< | grep 'Wrote: ' | sed 's/Wrote: //') $(BUILDDIR)

%.src.rpm: %.spec
	cp -a $(shell rpm -bs $< | grep 'Wrote: ' | sed 's/Wrote: //') $(BUILDDIR)

clean:
	rm -f $(BUILDDIR)/*