#!/bin/bash
echo "$1"
echo $#
if [ "$#" -ne 1 ] ; then
  echo "Usage: $0 commit_message" >&2
  exit 1
fi

message="$1"
echo message
echo "commiting code to github..."

project_root=$(pwd)
echo $project_root
cd $project_root
git pull --no-ff --no-edit
git add -A .
#git add -A ..
git commit -m "$message"
git push

echo "pushing code to github..."
