# Web Stack debugging increase limit of open files per user
exec { 'change-os-configuration-for-holberton-user':
  environment => ['DIR=/etc/security/limits.conf',
                  'OLD=hard nofile 5',
                  'NEW=hard nofile 50000',
                  'OLD2=soft nofile 4"',
                  'NEW2=soft nofile 40000'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo sed -i "s/$OLD2/$NEW2/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
