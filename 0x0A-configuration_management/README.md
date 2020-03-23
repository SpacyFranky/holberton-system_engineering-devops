# 0x0A Configuration management
# Requirements
* All files were interpreted on Ubuntu 14.04 LTS
* All files end with a new line
* My Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* My Puppet manifests must run without error
* My Puppet manifests first line is a comment explaining what the Puppet manifest is about
* My Puppet manifests files must end with the extension .pp
# Install ```puppet-lint```
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```