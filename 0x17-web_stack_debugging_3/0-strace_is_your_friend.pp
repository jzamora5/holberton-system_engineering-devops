# Web Stack debugging fix typo in config file
exec { 'fix_typo':
  environment => ['DIR=/var/www/html/wp-settings.php'],
  command     => 'sudo sed -i "s/class-wp-locale.phpp;/class-wp-locale.php;/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0,1]
}
