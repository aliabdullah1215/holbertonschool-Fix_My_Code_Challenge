#!/usr/bin/env ruby

ARGV.map(&:to_i).sort.each do |n|
  puts n
end
