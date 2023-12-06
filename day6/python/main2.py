import sys

line = sys.stdin.readline()
ts = [int(line.removeprefix("Time:").strip().replace(" ", ""))]

line = sys.stdin.readline()
ds = [int(line.removeprefix("Distance:").strip().replace(" ", ""))]

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
