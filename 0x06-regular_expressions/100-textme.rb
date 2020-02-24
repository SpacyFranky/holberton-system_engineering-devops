#!/usr/bin/env ruby
print (ARGV[0].scan(/(?<=from:)[a-zA-Z]*/).join)
print ","
print (ARGV[0].scan(/(?<=to:)[+][0-9]*/).join)
print ","
print (ARGV[0].scan(/(?<=flags:)(...)(...)(...)(...)/).join)
puts
