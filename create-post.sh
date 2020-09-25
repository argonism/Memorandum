
#!/bin/bash
# create article with title

if [ $# -lt 1 ]; then
  echo 'usage: sh create-post.sh {title} {category} {tag}'
  echo "title is required.\n"
  exit 1
fi

ShapeTitle () {
    echo $1 | sed 's/[\. ]/-/g'
}

DATE=`date '+%Y-%m-%-d'`
YEAR=`date '+%Y'`
TITLE=`ShapeTitle "$1"`

# set Category
CATEGORY=$2
if [ -z "$CATEGORY" ]; then
  CATEGORY="Diary"
fi

# set Tags
if [ $# -lt 3 ]; then
    TAGS="\n    - \"new\""
fi

for x in "${@:3:($#)}"
do
    TAG="\n    - \"${x}\""
    TAGS=$TAGS$TAG
done

# set filename
FORMAT="+%Y-%m-%-d--${TITLE}"
FILENAME=`date ${FORMAT}`

# set generate target path
SCRIPT_DIR=$(cd $(dirname $0); pwd)
ARTICLE_PATH="${SCRIPT_DIR}/content/blog/${YEAR}/${FILENAME}.md"

# avoid overwrite
if [ -f $ARTICLE_PATH ]; then
  echo "${FILENAME} already existed."
  exit 1
fi

echo "---
title: ${TITLE}
date: '${DATE}'
draft: false
category: '${CATEGORY}'
tags: ${TAGS}
cover: '../media/'
---" > $ARTICLE_PATH

code $ARTICLE_PATH