#!/bin/bash

OUTPUT_FILENAME="output"
TEMPLATE_FILENAME="template.tex"

cat meta.md sections/*.md > $OUTPUT_FILENAME.md
pandoc $OUTPUT_FILENAME.md -t pdf -o $OUTPUT_FILENAME.pdf --template $TEMPLATE_FILENAME
