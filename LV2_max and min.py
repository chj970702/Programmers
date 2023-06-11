def solution(s):
    li = s.split()
    check = []
    for item in li:
        item = int(item)
        check.append(item)
    answer = []
    answer.append(str(min(check)))
    answer.append(' ')
    answer.append(str(max(check)))
    result = ''
    for item in answer:
        result += item
    return result