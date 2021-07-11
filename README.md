# Lab report template for pandoc

This is a template for lab reports, for using with `pandoc`.
(Well, not just for lab reports, can be used for project reports as well.)

Just write your report in markdown format, and use `pandoc` to convert to pdf.

The LaTeX template for `pandoc` ([template.tex](./template.tex)) is based on the [default template](https://github.com/jgm/pandoc/blob/master/data/templates/default.latex).

[meta.md](./meta.md) contains YAML metadata; variables can be changed in the
file. The variables I've used there are just a few of the ones available,
[variables.md](./variables.md) contains all the variables that I was able to
scrape with my scraper script.

Contents of the report go in `sections` directory. Either make a huge file with
everything in a single place, or split the contents into many files as you like (but be sure to
name them in alphabetical order, that's how the files are picked). Also, all the
files must be in markdown format with `.md` extension.

[build.sh](./build.sh) script takes care of ~~concatenating~~ merging files and converting to
pdf with `pandoc`. Execute it without any arguments (pun not intended).

There are plenty of things to do, but it works right away. It's not perfect, but
it works.

## To Do:
- [ ] Modify the variable scraper (don't know if that's thing, I used the term without thinking) script to separate the variables I added myself from the variables in default template.
- [ ] Add variables for university and campus names.
