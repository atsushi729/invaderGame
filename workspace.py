member = int(input())
mlist = []
mcount = []
for i in range(member):
    mlist.append(int(input()))

process = int(input())

for i in range(process):
    mcount = input().split()
    target = int(mcount[1])
    sender = int(mcount[0])
    ball = int(mcount[2])

    if mlist[sender - 1] >= ball:
        mlist[target - 1] += ball
        mlist[sender - 1] -= ball
    else:
        mlist[target - 1] += mlist[sender - 1]
        mlist[sender - 1] = 0

for i in mlist:
    print(i)
