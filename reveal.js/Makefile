slides.html: slides.md
	pandoc --to=revealjs --standalone --css=mywhite.css -o $@ $<

.PHONY: clean
clean:
	rm slides.html
