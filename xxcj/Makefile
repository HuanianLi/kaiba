TARGETS	= run \
	  xxcjfoo

all: $(TARGETS)

%: %.sh
	cp $< $@ && chmod +x $@

%: %.py
	cp $< $@ && chmod +x $@

clean:
clobber: clean
	rm -f $(TARGETS)

cl: clobber
