from termcolor import colored

def sum_two_integers(int1, int2):
  summ = int1 + int2
  print(colored(f"Sum of {int1} and {int2} = {summ}", "red" if summ < 0 else "green"))
  return summ
