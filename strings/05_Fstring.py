import random

message = "Congratulations {}!, U just won urself {}$ Dollars"

player_1 = "Arsh Khan"
player_2 = "Morock Gamer"
player_3 = "Cruel Ocean"

reward = random.randint(1, 100)*100

reward_player_1 = message.format(player_1, reward)
reward = random.randint(1, 100)*100


print(reward_player_1)


#this is very lenght and time wasting

print(f"Congratulations {player_2}!, U just won urself {reward}$ Dollars")
reward = random.randint(1, 100)*100
print(f"Congratulations {player_3}!, U just won urself {reward}$ Dollars")
