# kills the 'killmenow' process
exec { 'pkill -f killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
