#!/usr/bin/perl
use strict;
use warnings;

my $filename = "grades.txt";

open(my $file, '<',$filename) or die "cannot open file $filename:
$!\n";

my %grades;

while (my $line = <$file>){
	chomp($line);
	my ($name, $grade) = split(/\s+/, $line);
	if (!defined($grade)){
		die "expecting grade after name";
	}
	chomp($grade);
	
	$grades{$name} = $grade;
}
close $file;
print "enter a students name: ";
my $studentname = <STDIN>;
chomp($studentname);
if (exists $grades{$studentname}) {
	print "$studentname: $grades{$studentname}\n";
}
else {
	die "name does not exist";
}
exit 0;

