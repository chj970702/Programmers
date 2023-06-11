def solution(s):
    answer = ''
    check = list(s.lower())
    print(check)
    for i in range(len(check)):
        if check[i].isdigit():
            answer += s[i]
        elif check[i] == ' ':
            answer += s[i]
        elif check[i].isalpha():
            if len(check[0:i]) == 0:
                answer += check[i].upper()
            elif check[i-1] == ' ':
                answer += check[i].upper()
            else:
                answer += check[i]

    return answer


# print(solution("for the last week"))
# print(solution("3Abcdefg    aBC    DaB"))
