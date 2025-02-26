#!/usr/bin/perl
use strict;
use warnings;
#head.pl
#Author: Merrick Moncure
#Purpose: Read 10 lines from std input and print to std output
#!/usr/bin/perl

my $line_num = 0;

while (my $line = <STDIN>) {
    chomp($line);
    $line_num++;
    #loop thru stdin and print each line
    print "$line_num: $line\n";


    last if $line_num == 10;
}

if ($line_num > 0){
    exit(0); #success
} else{
    print STDERR "Error: Lines were not read.\n";
    exit(1);
}
