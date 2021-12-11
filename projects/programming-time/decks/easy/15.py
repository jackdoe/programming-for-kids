# roll() the dice untill you get a
# number bigger or equal to `min`.
# A function can call itself, This
# is called recursion.
def roll(min):
  dice = ⚂

  if dice < min:
    return roll(min)

  return dice

enemy_hp = 20
my_hp = 25

enemy_attack = roll(2)
player_attack = roll(7)

# keep attacking until either me or
# my enemy runs out of health points
while enemy_hp > 0 and my_hp > 0:
  enemy_hp -= player_attack
  my_hp -= enemy_attack

print(enemy_hp)
print(my_hp)
