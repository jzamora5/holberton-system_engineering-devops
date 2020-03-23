# Create a PP File
file { '/tmp/holberton':
  ensure  => file, # Makes sure File Exists
  path    => '/tmp/holberton', # PATH
  mode    => '0744',           # Permissions
  owner   => 'www-data',       # Owner
  group   => 'www-data',       # Group
  content => 'I love Puppet',  # Content
}
