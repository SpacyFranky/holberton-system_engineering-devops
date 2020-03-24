# Client configuration file (w/ Puppet)
server_options => {
  'Match User www-data' => {
    'PasswordAuthentication' => 'no',
    'IdentityFile' => '~/.ssh/holberton',
  }
}