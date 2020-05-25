# Web Stack debugging increase limit of open files per user
exec { 'fix-wordpress':
  environment => ['DIR=/etc/default/nginx',
                  'OLD=ULIMIT="-n 15"',
                  'NEW=ULIMIT="-n 15000"'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
