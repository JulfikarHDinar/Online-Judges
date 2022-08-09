n, m = input().split()
happiness=0
arr = input().split()
A = set(input().split())
B = set(input().split())

for i in arr:
  if i in A:
    happiness = happiness + 1

for i in arr:
  if i in B:
    happiness = happiness - 1

print(happiness)
