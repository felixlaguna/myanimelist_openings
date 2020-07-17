#!/bin/bash
find "$1" -type f -iname "*.webm" -exec bash -c 'FILE="$1"; TITLE="$(basename -- $FILE)";ffmpeg -i "${FILE}" -vn -ab 320k -ar 44100 -metadata artist=FLTAnime -metadata title="${TITLE%.webm}" -y "${FILE%.webm}.mp3"' _ '{}' \;
find "$1" -type f -iname "*.webm" -delete
