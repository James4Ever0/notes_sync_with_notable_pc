#!/bin/bash

cd /root/Desktop/works/notes_ssh_keys
# mkdir notes # now we only sync here.
# run this when notable is also running. otherwise, exit.
cd notes
# cd ~/.notable/notes


env GIT_SSH_COMMAND='ssh -i /root/Desktop/works/notes_ssh_keys/id_rsa_original_backup' git fetch -f origin master

git add .
current_date=$(date)
git commit -m "Update Notes $current_date"

env GIT_SSH_COMMAND='ssh -i /root/Desktop/works/notes_ssh_keys/id_rsa_original_backup' git push -f git@gitee.com:n5366871df2f3/notes.git master

### now do some backup.
# rclone sync -P . ~/.notable/notes
# failed completely. shit. we only do local backups? no more fucking webdav.
