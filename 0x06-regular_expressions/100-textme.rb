#!/usr/bin/env ruby
print (ARGV[0].scan(/(?<=from:)[a-zA-Z+0-9]*/).join)
print ","
print (ARGV[0].scan(/(?<=to:)[+0-9]*/).join)
print ","
print (ARGV[0].scan(/(?<=flags:)(?<=flags:).[0-1:-]*/).join)
puts
