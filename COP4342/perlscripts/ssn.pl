#!/usr/bin/perl
use strict;
use warnings;

#ssn.pl
#Author: Merrick Moncure
#purpose: reads in a list of ssn numbers and prints them with their matching names

#check if there is a file
if (@ARGV != 1) {
    die "usage: ssn.pl filename\n";
}

my $filename = $ARGV[0];

open(my $fh, '<', $filename) or die "cannot open file $filename: $!\n";

my %ssn_hash;

while (my $ssn = <$fh>) {
	chomp($ssn);
	my $name = <$fh>;

	if (!defined($name)){
		die "Expecting a name after the ssn $ssn.\n";
	}

	chomp($name);

	if (exists $ssn_hash{$ssn}) {
	    die "$ssn already exists for $ssn_hash{$ssn}.\n";
	}

	$ssn_hash{$ssn} = $name;
}

close($fh);

#sort the ssns
foreach my $ssn (sort keys %ssn_hash) {
	print "$ssn: $ssn_hash{$ssn}\n";
}

exit 0;
