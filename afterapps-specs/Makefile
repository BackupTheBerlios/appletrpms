RPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/i586.rpm/')
SRPMS=$(shell ls *.spec | grep -v base.spec | sed 's/spec/src.rpm/')
RPMDIR=rpmdir
SRPMDIR=srpmdir

all: rpms srpms hdlist

rpms: $(RPMDIR) $(RPMS) 

srpms: $(SRPMDIR) $(SRPMS)

hdlist: $(RPMDIR) $(SRPMDIR) 
	cd $(RPMDIR) && genhdlist .
	cd $(SRPMDIR) && genhdlist .

$(RPMDIR):
	mkdir -p $(RPMDIR)

$(SRPMDIR):
	mkdir -p $(SRPMDIR)

%.i586.rpm: %.spec
	cp -a $(shell rpm -bb $< | grep 'Wrote: ' | sed 's/Wrote: //') $(RPMDIR)

%.src.rpm: %.spec
	cp -a $(shell rpm -bs $< | grep 'Wrote: ' | sed 's/Wrote: //') $(SRPMDIR)

clean:
	rm -f $(RPMDIR)/* $(SRPMDIR)/*