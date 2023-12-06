import sys

line = sys.stdin.readline()
ts = list(map(int, line.removeprefix("Time:").split()))

line = sys.stdin.readline()
ds = list(map(int, line.removeprefix("Distance:").split()))

p = 1
for t, d in zip(ts, ds):
    s = 0
    for i in range(t):
        startup_time = i + 1
        travel_time = t - startup_time
        speed = startup_time
        if speed * travel_time > d:
            s += 1
    p *= s

print(p)
