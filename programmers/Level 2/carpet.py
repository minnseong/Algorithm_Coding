# Programmers 01/23 2021
# 카펫

def solution(brown, yellow):
    answer = []
    yellow_list = []
    # yellow 약수 구하기
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_list.append(i)

    for i in range(0, len(yellow_list)):
        for j in range(i, len(yellow_list)):
            yaksu_1 = yellow_list[i]
            yaksu_2 = yellow_list[j]

            if (yaksu_1 * yaksu_2) == yellow:
                if (yaksu_1 + yaksu_2) * 2 + 4 == brown:
                    if yaksu_1 > yaksu_2:
                        answer.append(yaksu_1 + 2)
                        answer.append(yaksu_2 + 2)
                        break
                    else:
                        answer.append(yaksu_2 + 2)
                        answer.append(yaksu_1 + 2)
                        break
    return answer

print(solution(24, 24))

# ㅁㅁㅁㅁㅁㅁ   ㅁㅁ (1+2)2 + 4
# ㅁㅁㅁㅁㅁㅁ
# ㅁㅁㅁㅁㅁㅁ
# ㅁㅁㅁㅁㅁㅁ
# (가로 + 세로) * 2 + 4 = brown
# (yaksu_1 + yaksu_2) * 2 + 4 == brown
# 8+12+4