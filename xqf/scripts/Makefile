TARGETS	= fang \
	  run_fang \
	  bank \
	  run_bank \
	  long6 \
	  run_long6


all: ${TARGETS}

%: %.py
	cp $< $@ && chmod +x $@

%: %.sh
	cp $< $@ && chmod +x $@

clean:
clobber: clean
	rm -f ${TARGETS}
cl: clobber
