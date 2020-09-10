
#!/bin/bash
# create article with title

files="/home/user/*"
SCRIPT_DIR=$(cd $(dirname $0); pwd)
FILES_DIR="${SCRIPT_DIR}/content/blog/2020/ksnctf/*"
for filepath in $FILES_DIR; do
    ARTICLE_PATH="${filepath}/write_up.md"
    if ! [ -f $ARTICLE_PATH ]; then
        echo "${ARTICLE_PATH} doesn't exist"
        continue
    fi

    DATE=`date -r ${ARTICLE_PATH} '+%Y-%m-%-d'`
    Q_NUM=`basename ${filepath}`
    TITLE="ksnctf Q.${Q_NUM}"
    sed -i -E "s/title:.*$/title: ${TITLE}/" ${ARTICLE_PATH}
    sed -i -E "s/date: [\"']{2}/date: \"${DATE}\"/" ${ARTICLE_PATH}
    sed -i -E "s/category: [\"']{1}Diary[\"']{1}/category: \"CTF\"/" ${ARTICLE_PATH}
    sed -i -E "s/    - [\"']{1}new[\"']{1}/    - \"ksnctf\"/" ${ARTICLE_PATH}
    echo "${Q_NUM} was overwritten"
done