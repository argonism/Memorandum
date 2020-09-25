
#!/bin/bash
# create article with title

ShapeTitle () {
    echo $1 | sed 's/[\. ]/-/g'
}

DATE=`date '+%Y-%m-%-d'`
YEAR=`date '+%Y'`
if [ $# -lt 1 ]; then
  echo 'usage: sh create-post.sh {title} {category} {tag}'
  echo "title is required.\n"
  exit 1
fi
TITLE=`ShapeTitle "$1"`

CATEGORY=$2
if [ -z "$CATEGORY" ]; then
  echo "Diary"
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
category: '${CATEGORY}'
tags:
  - 'new'
cover: '../media/'
---" > $ARTICLE_PATH

code $ARTICLE_PATH