# notes_sync_with_notable_pc
sync notes via git service provider while notable is running

## example usage

```bash
#!/bin/bash
#umount ~/.notable
# kill all zombie notables. may kill this app in other windows.
ps aux | grep -i notable | grep opt | awk '{print $2}' | xargs -iabc kill -s KILL abc
ps aux | grep -i sync_notes | grep opt | awk '{print $2}' | xargs -iabc kill -s KILL abc

curl https://www.baidu.com >/dev/null
if [ "$?" -ne 0 ]; then
        echo "NO INTERNET. PROGRAM WILL EXIT."
        exit
fi

# make sure that you have internet!
# execute sync_notes.
python3 /root/Desktop/works/notes_ssh_keys/sync_notes.py &

/usr/bin/notable_bin --no-sandbox $@
```
