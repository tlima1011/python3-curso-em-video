from time import sleep
import emoji
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':fireworks:BOOM! :fireworks:BUM!:fireworks:POOOW!:fireworks:', use_aliases=True))

for i in range(0, 10):
    sleep(5)
    print(emoji.emojize(':fireworks:BOOM! :fireworks:BUM!:fireworks:POOOW!:fireworks:', use_aliases=True))

