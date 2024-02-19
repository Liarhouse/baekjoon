def solve_linear_system(a, b, c, d, e, f):
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if a*i + b*j == c and d*i + e*j == f:
                return f"{i} {j}"
    return "해가 존재하지 않습니다."

# 사용자로부터 6개의 정수 입력 받기
a, b, c, d, e, f = map(int, input().split())

# 선형 방정식 시스템 해결하고 결과 출력
print(solve_linear_system(a, b, c, d, e, f))
