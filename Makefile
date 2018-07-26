all: foo

%: %.py
	cp $< $@ && chmod +x $@

clean:

clobber: clean
	rm -f foo
