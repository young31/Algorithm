words = ["frodo", "front", "frost", "frozen", "frame", "kakao", "k", "qwdf", "dddasf"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]

# trie 구조를 공부하고 이 문제를 해결할 수 있겠다고 생각이 들었다.
# 역방향 구현 및 글자 수에 따라서 분할해서 class 생성
class Node:
    def __init__(self, key, data=None, cnt=1):
        self.key = key # char
        self.data = data
        self.cnt = cnt      
        self.children = {}
    
class Trie:
    def __init__(self):
        self.head = Node(None, None, 0)
        self.memory = {}
        
    def insert(self, strs):
        cur = self.head
        for s in strs:
            if s not in cur.children.keys():
                cur.children[s] = Node(key=s, cnt=1)
            else:
                cur.children[s].cnt += 1
        
            cur = cur.children[s]
        
        cur.data = strs

    def search(self, strs):
        if strs in self.memory.keys():
            return self.memory[strs]

        cur = self.head
        for s in strs:
            if s != '?':
                if s not in cur.children:
                    return 0
                else:
                    cur = cur.children[s]
            else:
                if cur == self.head:
                    return sum([cur.children[x].cnt for x in cur.children])
                self.memory[strs] = cur.cnt
                return cur.cnt

def solution(words, queries):
    answer = []

    trie_head = {}
    trie_tail = {}
    for word in words:
        n = len(word)
        if n not in trie_head.keys():
            trie_head[n] = Trie()
            trie_tail[n] = Trie()
        
        trie_head[n].insert(word)
        trie_tail[n].insert(word[::-1])

    print(trie_head)
    for querie in queries:
        n = len(querie)
        if n not in trie_head.keys():
            answer.append(0)
        else:
            if querie[0] != '?':
                trie = trie_head[n]
                answer.append(trie.search(querie))
            else:
                trie = trie_tail[n]
                answer.append(trie.search(querie[::-1])) 

    print(answer)
    return answer

solution(words, queries)