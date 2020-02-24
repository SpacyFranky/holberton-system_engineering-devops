# 0x06. Regular expression
# Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```
# Requirements
* Used editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 14.04 LTS
* All files should end with a new line
* All Bash script files are executable
* The first line of all  Bash scripts is exactly #!/usr/bin/env ruby
* All regex are built for the Oniguruma library