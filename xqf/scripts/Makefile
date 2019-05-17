TARGETS	= fang \
	  run_fang \
	  bank \
	  run_bank


all: ${TARGETS}

%: %.py
	cp $< $@ && chmod +x $@

%: %.sh
	cp $< $@ && chmod +x $@

clean:
clobber: clean
	rm -f ${TARGETS}
cl: clobber
