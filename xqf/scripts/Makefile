TARGETS	= fang run_fang

all: ${TARGETS}

%: %.py
	cp $< $@ && chmod +x $@

%: %.sh
	cp $< $@ && chmod +x $@

clean:
clobber: clean
	rm -f ${TARGETS}
cl: clobber
