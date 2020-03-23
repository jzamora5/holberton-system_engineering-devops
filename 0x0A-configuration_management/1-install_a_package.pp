# Install puppet-lint 2.1.1 with Puppet
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => gem,
}
