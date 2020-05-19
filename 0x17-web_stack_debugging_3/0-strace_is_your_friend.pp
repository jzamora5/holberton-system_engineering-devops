# Web Stack debugging fix typo in config file
file_line { 'fix_wp_typo':
  ensure            => 'present',
  path              => '/var/www/html/wp-settings.php',
  line              => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match             => "^require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  replace           => true,
  match_for_absence => false,
}
