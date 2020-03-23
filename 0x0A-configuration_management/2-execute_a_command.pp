# create a manifest that kills a process named "killmenow"
exec { 'pkill -f ./killmenow':
  path    => ['/user/bin', '/usr/sbin',],
}