#!/usr/bin/env ruby

ARGV.select { |arg| arg.match?(/^[-]?\d+$/) }
    .map(&:to_i)
    .sort
    .each { |n| puts n }
