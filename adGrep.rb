#!/usr/bin/env ruby

regexp = Regexp.new(ARGV[0])

while ( line = $stdin.gets )
  match = regexp.match(line)
  if match
    puts match[1..-1].join(" ")
  end
end
