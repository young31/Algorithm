words = ["word","war","warrior","world"]

# Trie 라는 구조에 대해서 처음 알게 됨
# 단어 일치 등에 대한 문제는 이런 방식을 사용!
class Node:
    def __init__(self, key, data=None, cnt=1):
        self.key = key # char
        self.data = data
        self.cnt = cnt      
        self.children = {}
    
class Trie:
    def __init__(self):
        self.head = Node(None, None, 0)
        
    def insert(self, strs):
        cur = self.head
        for s in strs:
            if s not in cur.children.keys():
                cur.children[s] = Node(key=s, cnt=1)
            else:
                cur.children[s].cnt += 1
        
            cur = cur.children[s]
        
        cur.data = strs
        
    
def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
        
    for word in words:
        m = len(word)
        cur = trie.head
        i = 0
        for w in word:
            i += 1
            if cur.children[w].cnt == 1:
                break
            cur = cur.children[w]
        answer += i
    print(answer)
    return answer

solution(words)