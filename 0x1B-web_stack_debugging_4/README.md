## 0x1B - Web Stack Debugging 4

This script sets the maximum open file count of an nginx server to 4096

# Process
`ab -c 100 -n 2000 localhost/` showed that about half of requests were being denied

`ps aux | grep nginx` showed nginx processes that were running

in order to see the limits that nginx had set, used `cat /proc/[PID of nginx process]/limits`

discovered that `Max open files` had been set to 15

changed /etc/defaults/nginx file to restore default ULIMIT to 4096
