# 입력최적화를 하고 출력최적화 했는데도 안풀림
import sys

n = int(input())
# arr = [0] * n
# for i in range(n):
#     arr[i] = int(input())
arr = sys.stdin.read().readlines()

arr.sort()
# sys.stdout.write("\n".join(str(arr[x]) for x in range(len(arr))) + "\n")
# for i in arr:
#     print(i)
s = ""
for i in arr:
    s += str(i) + "\n"
print(s)
