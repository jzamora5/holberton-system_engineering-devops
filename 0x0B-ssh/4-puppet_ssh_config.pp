# Manifest to modify SSH config file
exec { 'echo':
  command => 'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => 'usr/bin:/bin',
  returns => [0,1],
}
