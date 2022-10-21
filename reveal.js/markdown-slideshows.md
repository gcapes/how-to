# Slideshows from markdown using reveal.js

I think this is mainly aimed at an audience who are comfortable writing html. However, I've figured out from a few sources how to create a reveal.js slideshow from markdown using pandoc, and how to edit a css file to customise the theme.

## Using defaults

You need [pandoc](https://pandoc.org/installing.html) installed, and a markdown file. 

Basic compilation uses 

```
pandoc -t revealjs -s -o index.html slides.md 
```

This compiles using the current version of reveal.js on their server, and the default theme. The fonts are too big and it looks silly, so we'll need to download a copy of reveal.js and make a custom theme.

## Custom theme

Themes are at `reveal/dist/theme/`. I made a copy of the `white.css` theme and modified the font size and capitalisation settings.

Compilation then becomes:

```
pandoc -t revealjs -s -o index.html slides.md -V revealjs-url=./reveal.js -V theme=mywhite
```

## One central copy of reveal.js?

The above works, but needs the `revealjs-url` option to point to the local installation. Wouldn't it be nice to just have one copy of reveal.js and not need to tell pandoc where it is? [Apparently](https://stackoverflow.com/a/24448695) if reveal.js is put in the pandoc user data directory (given in the output from `pandoc --version`) we can then reduce the above to:

```
pandoc -t revealjs -s -o index.html slides.md -V theme=mywhite
```

However, it didn't work for me.

## TL;DR just use the `--css` option

I've been using the above approach for a while, but have just found out there is a pandoc option to directly specify a custom css file, without having to have a copy of reveal.js locally.  We can then dispense with the `theme=` reveal.js variable.

```
pandoc -t revealjs -s -o slides.html -c mywhite.css slides.md
```

Or using the more verbose form:

```
pandoc --to=revealjs --standalone --css=mywhite.css -o slides.html slides.md
```

This is a much lighter-touch solution and is particularly useful when hosting on github, and means you don't have to keep reveal.js updated either. Just need to push the css file so the slideshow works.
