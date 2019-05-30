# This script resets the ULIMIT of the nginx process to 4096
# (recommended default)
exec { '/etc/default/nginx':
  command => 'sed -i s/15/4096/g /etc/default/nginx; \
  /etc/init.d/nginx restart',
  path    => ['/bin/'],
}
