#!/bin/bash

cd /root/Desktop/works/notes_ssh_keys
# mkdir notes # now we only sync here.
# run this when notable is also running. otherwise, exit.
cd notes
# cd ~/.notable/notes


env GIT_SSH_COMMAND='ssh -i /root/Desktop/works/notes_ssh_keys/id_rsa_original_backup' git pull --force origin master

