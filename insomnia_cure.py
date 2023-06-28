k=int(input()) #punched in the face with a frying pan
l=int(input()) #got his tail shut into the balcony door
m=int(input()) #got his paws trampled with sharp heels
n=int(input()) #threatened every n-th dragon to call her mom, and he withdrew in panic
d=int(input()) #total

damaged_dragons = 0

for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        damaged_dragons += 1

print(damaged_dragons)