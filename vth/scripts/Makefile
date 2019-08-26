TARGETS	= vth_ids

all: $(TARGETS)

%: %.sh
	cp $< $@ && chmod +x $@

clean:
clobber: clean
	rm -f $(TARGETS)
cl: clobber
