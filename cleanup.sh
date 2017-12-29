#!/usr/bin/env bash
sed -i -n '/End of the Project Gutenberg EBook/q;p' $1
sed -i -n '/^FOOTNOTES: /q;p' $1
sed -i '/START OF THIS PROJECT GUTENBERG EBOOK /,$!d' $1
sed -i 's/[^a-z ]/ /gI' $1 

