#!/usr/bin/perl
use strict;
use warnings;
use Text::Wrap;

my %word_freq;

while (<>) {
    #convert to lowercase
    while (/([a-zA-Z]{2,})/g) {
        my $word = lc $1;
        $word_freq{$word}++;
	}
}

my %freq_to_words;
foreach my $word (keys %word_freq) {
	my $freq = $word_freq{$word};
	push @{$freq_to_words{$freq}}, $word;
}

#sort the frequencies
my @freqs = sort { $b <=> $a } keys %freq_to_words;

print "frequency index\n";
print "---------------\n";
#handle empty input
if (!@freqs) {
    print "-1-\n";
    exit;
}

#wrap the text
$Text::Wrap::columns = 80;

#print the frequencies
foreach my $freq (@freq) {
    my @words = sort @{$freq_to_words{$freq}};
    my $joined = join(', ', @words);
    my $wrapped = wrap("$freq: ", "	", $joined);
    print $wrapped . "\n";
}
