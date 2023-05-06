use strict;
use warnings;

sub sum_of_digits_pow5 {
  my $n = shift;
  my $s = 0;
  while ($n > 0) {
    $s = $s + ($n % 10)**5;
    $n = int($n / 10);
  }
  return $s;
}

my @list = ();
for (my $i = 2; $i < 1000000; $i++) {
  if ($i == sum_of_digits_pow5 $i) {
    push @list, $i;
  }
}

my $sum = 0;
foreach my $n (@list) {
  $sum += $n;
}

print "$sum"
