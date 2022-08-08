from sum_of_two.sum import sum_two_integers

def test_sum_greater_than_zero():
  assert sum_two_integers(2,2) == 4

def test_sum_less_than_zero():
  assert sum_two_integers(2, -10) == -8
