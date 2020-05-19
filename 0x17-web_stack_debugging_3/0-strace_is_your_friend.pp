# Web Stack debugging fix typo in config file
exec { 'fix_typo':
  environment => ['DIR=/var/www/html/wp-settings.php',
                  "L=require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
                  "LF=require_once( ABSPATH . WPINC . '/class-wp-locale.php' );"],
  command     => 'sudo sed -i "s/$L;/$LF;/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0,1]
}
