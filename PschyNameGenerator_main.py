"""Generate sidekick names based from the Psych tv show"""

import sys
import random

def main():
  print("Welcome to the Psych Sidekick Name Generator")
  print("A name just like Sean would pick for Gus:\n\n'")
  
  first = ('SuperSmeller','Francois','Peter Panic','Felicia','Gus','Ovaltine','Shmuel','Magic','Don','Galileo','The','Schoonie','Lavender','Hummingbird','Scrooge','Sterling','Dr.','Step','Trapezious','Jazz','Doughnut','Clemintine','The Vault Of','Ghee','Pennywhistle', 'Pitchfork Ben', 'Potato Bug','Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
"Winston 'Jazz Hands'", 'Worms')
  last = ('Fancybottom', 'Smeller','Lambert Watkins','T.T Showbiz','Jenkins','Cohen','Head','Humpkins','Jackal','U-turn SIngleton','Gooms','Honeysuckle','Saltalamacchia','Jones','Hollabackatcha','Slicks','Cooper','Milkington','Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles','Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf','Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'Sugar­Gold', 'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
'Woolysocks')

  while True:
    first_name = random.choice(first)
    last_name = random.choice(last)

    print("\n\n")
    print("{} {}".format(first_name, last_name), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

    if try_again.lower() == "n":
      break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()