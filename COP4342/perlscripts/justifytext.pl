#!/usr/bin/perl
use strict;
use warnings;
#justifytext.pl
#Author: Merrick Moncure
#purpose: justifies text from stdin
#read input from standard input
chomp(my $input_file = <STDIN>);
chomp(my $output_file = <STDIN>);
chomp(my $max_width = <STDIN>);

#open input and output files
open my $in, '<', $input_file or die "Cannot open input file: $!\n";
open my $out, '>', $output_file or die "Cannot open output file: $!\n";

my @paragraph;

while (<$in>) {
    chomp;
    if (/^\s*$/) {
        process_paragraph(\@paragraph, $out, $max_width) if @paragraph;
        print $out "\n";
        @paragraph = (); #reset for next paragraph
    } else {
        push @paragraph, split /\s+/;
    }
}
process_paragraph(\@paragraph, $out, $max_width) if @paragraph;

close $in;
close $out;

sub process_paragraph {
    my ($words_ref, $out, $max_width) = @_;
    my @words = @$words_ref;
    my @line;
    my $line_length = 0;

    while (@words) {
        my $word = shift @words;
        
        if ($line_length + length($word) + scalar(@line) > $max_width) {
            justify_line(\@line, $out, $max_width);
            @line = ($word);
            $line_length = length($word);
        } else {
            push @line, $word;
            $line_length += length($word);
        }
    }
    print $out join(" ", @line) . "\n" if @line; #print the last line normally
}

sub justify_line {
    my ($line_ref, $out, $max_width) = @_;
    my @line = @$line_ref;
    return print $out join(" ", @line) . "\n" if @line == 1; # Single word
    
    my $total_length = 0;
    $total_length += length($_) for @line;
    my $spaces_needed = $max_width - $total_length;
    my $gaps = @line - 1;
    my @spaces = ( (" " x int($spaces_needed / $gaps)) ) x $gaps;
    
    for my $i (0 .. ($spaces_needed % $gaps) - 1) {
        $spaces[$gaps - 1 - $i] .= " ";
    }
    
    my $justified_line = "";
    for my $i (0 .. $#line - 1) {
        $justified_line .= $line[$i] . $spaces[$i];
    }
    $justified_line .= $line[-1];
    
    print $out "$justified_line\n";
}

