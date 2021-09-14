def solution(s):
    key_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    answer = ''
    for k, v in key_map.items():
        s = s.replace(k, v)
    return int(s)