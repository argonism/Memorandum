
#!/bin/bash
# create article with title

DATE=`date '+%Y-%m-%-d'`
YEAR=`date '+%Y'`
TITLE=$1
if [ $# -lt 1 ]; then
  echo 'usage: {this program} {title} {category} {tag}'
  echo "title is required to create article.\n"
  exit 1
fi
FORMAT="+%Y-%m-%-d--${TITLE}"
FILENAME=`date ${FORMAT}`

SCRIPT_DIR=$(cd $(dirname $0); pwd)
ARTICLE_PATH="${SCRIPT_DIR}/content/blog/${YEAR}/${FILENAME}.md"

if [ -f $ARTICLE_PATH ]; then
  echo "${FILENAME} already existed."
  exit 1
fi

echo "---
title: ${TITLE}
date: '${DATE}'
draft: false
category: 'Diary'
tags:
  - 'new'
cover: '../media/'
---" > $ARTICLE_PATH

code $ARTICLE_PATH