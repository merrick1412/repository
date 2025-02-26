#!/usr/bin/perl
use strict;
use warnings;

#middle.pl
#Author: Merrick Moncure
#purpose: print the middle of input lines, with a line count argument optionally

my $num_lines = 10;
#@argv checks if there is args, the regex is looking for a dash followed by digits. like -10.
if (@ARGV && $ARGV[0] =~ /^-(\d+)$/) {
    $num_lines = $1;
    shift @ARGV;
}

#read all input into array
my @lines = <>;
#perl equivalent of .size()
my $total_lines = scalar @lines;

#edge case handling
if ($total_lines == 0) {
    print STDERR "Error: no input lines.\n";
    exit(1);
}

if ($total_lines <= $num_lines) {
    #if theres less lines than requested, print all the lienes
    print @lines;
    exit(0);
}


#get start and end index
my $sindex = int(($total_lines - $num_lines) / 2);
my $eindex = $sindex + $num_lines - 1;

#print the lines with a for loop
for my $i ($sindex .. $eindex) {
    print$lines[$i];
}

#if we got here everything went well
exit(0); 
