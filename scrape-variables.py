#!/bin/python3

# import sys
import re

INPUT_FILE = "template.tex"
PATTERN = r"\$(if|for)\((\w-?)+\)\$"

target = ""

if_vars = set()
for_vars = set()

with open(INPUT_FILE) as f:
    target = f.read()

for i in re.finditer(PATTERN, target):
    match = i.group()
    if "$if" in match:
        if_vars.add(match.split("(")[1][:-2])
    else:
        for_vars.add(match.split("(")[1][:-2])


def convert_to_md_list(item):
    item = ["* " + var for var in item]
    item_str = "\n".join(item)
    return item_str


with open("variables.md", "w") as f:
    f.write("# If vars:\n" + convert_to_md_list(if_vars))
    f.write("\n\n")
    f.write("# For vars:\n" + convert_to_md_list(for_vars))
