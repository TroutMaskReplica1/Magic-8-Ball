import random

choices = ['\nIt is certain', '\nIt is decidedly so', '\nWithout a doubt', '\nYes definitely', '\nYou may rely on it', '\nAs I see it, yes', '\nMost likely', '\nOutloook good', '\nYes', '\nNo', '\nReply hazy try again', '\nAsk again later', '\nBetter not tell you now', '\nCannot predict now', '\nConcentrate and ask again', '\nDont count on it', '\nMy reply is no', '\nMy sources say no', '\nOutlook not so good', '\nVery doubtful' ]

print('Welcome, ask a question')
x = input('ask here ')
while x != 'done':
    print(random.choice(choices))
    x = input('ask here ')