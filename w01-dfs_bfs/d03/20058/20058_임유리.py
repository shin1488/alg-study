# 엣지케이스 : 칸이 전체크기와 같을때
# 이중 포문으로 격자를 하나하나 회전(topright, topleft, botright, botleft)
# 모서리부터 얼음이 줄어들 예정

import sys
import math

input = sys.stdin.readline

ice = []

n, q = map(int, input().split())
# 얼음판
icesize = pow(2, n)
# 격자크기. 나중에 magic 만큼 바꿔야함
nemo = 2
for i in range(icesize):
    line = list(map(int, input().split()))
    ice.append(line)

magic = list(map(int, input().split()))


def firestorm(nemo):
    # 칸 회전, 칸 크기만큼 step
    for i in range(0, icesize, nemo):
        # 일단 2*2부터 돌려보고 4*4로 확장
        for j in range(0, icesize, nemo):
            # 시계방향
            left_top = ice[i][j]
            right_top = ice[i][j + 1]
            right_bottom = ice[i + 1][j + 1]
            left_bottom = ice[i + 1][j]

            ice[i][j + 1] = left_top
            ice[i + 1][j + 1] = right_top
            ice[i + 1][j] = right_bottom
            ice[i][j] = left_bottom
    # 녹이기 전 얼음판 확인
    for row in ice:
        print(row)
    print()
    melt = [[0] * icesize for _ in range(icesize)]
    # 녹일 칸을 저장하고 한번에 녹이기
    for i in range(icesize):
        for j in range(icesize):
            # 모서리면 바로 녹임 표시
            if (i == 0 or i == icesize - 1) and (j == 0 or j == icesize - 1):
                melt[i][j] = 1
                continue

            # 인접한 칸 얼음 여부
            count = 0
            # 왼쪽 칸
            if i - 1 >= 0:
                if ice[i - 1][j] > 0:
                    count = count + 1
            # 오른쪽 칸
            if i + 1 < icesize:
                if ice[i + 1][j] > 0:
                    count = count + 1
            # 위 칸
            if j - 1 >= 0:
                if ice[i][j - 1] > 0:
                    count = count + 1
            # 아래 칸
            if j + 1 < icesize:
                if ice[i][j + 1] > 0:
                    count = count + 1
            if count < 3:
                melt[i][j] = 1

    for i in range(icesize):
        for j in range(icesize):
            if ice[i][j] > 0 and melt[i][j] == 1:
                ice[i][j] = ice[i][j] - 1


for i in magic:
    firestorm(i)
    print(ice)
    print()
