import sys
import random

print("Welcome to the Psych Sidekick Name Generator")
print("A name that Shawn would give Gus:'\n'")


first = ()
last = ()

while true:
  first = random.choice(first)
  last = random.choice(last)

  print("\n\n")
  print("{}{}".format(first,last), file=sys.stderr)
  print("\n\n")

tryAgain = input("\n Try Again? press N to quit\n")
if tryAgain.lower == 'n':
  break
input("Press ENTER to exit\n")
