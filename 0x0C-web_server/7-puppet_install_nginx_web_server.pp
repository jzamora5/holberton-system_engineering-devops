# Manifest that configures NGINX
exec { 'exec_0':
  command => 'sudo sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'exec_1':
  require => Exec['exec_0'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'exec_2':
  require => Exec['exec_1'],
  command => 'echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'exec_3':
  require     => Exec['exec_2'],
  environment => ['GG=google.com permanent'],
  command     => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me $GG;/" /etc/nginx/sites-enabled/default',
  path        => ['/usr/bin', '/bin'],
  returns     => [0,1]
}

exec { 'exec_4':
  require => Exec['exec_3'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}
