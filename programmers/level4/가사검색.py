# -*- coding: utf-8 -*-

from collections import defaultdict

class Node:
    def __init__(self, char, length = None, word = None):
        self.char = char
        self.word = None
        self.children = {}
        # 길이가 length인 단어의 개수를 value로 가지는 dictionary. 
        # defaultdict을 사용해 인자값이 없으면 0을 리턴.
        self.length = defaultdict(int)

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, word):
        node = self.head
        node.length[len(word)] += 1
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            # 해당 노드를 거쳐가는 문자열 중 길이가 len(string)인 것의 개수를 저장.
            node.children[char].length[len(word)] += 1
            # 그 다음 children 노드로 이동
            node = node.children[char]
        # leaf 노드에 해당 단어를 저장
        node.word = word
        
    def start_with(self, prefix, length):
        node = self.head
        for char in prefix:
            if char in node.children:
                # 그 다음 children 노드로 이동
                node = node.children[char]
            else:
                return 0
        # prefix의 마지막 노드에서 length의 value를 확인해
        # 해당 노드를 거쳐간 문자열 중 길이가 length인 것의 개수를 반환.
        return node.length[length]

def solution(words, queries):
    answer = []
    front = Trie()
    back = Trie()
    for word in words:
        front.insert(word)
        back.insert(word[::-1])
    for word in queries:
        # 전부 ?일 경우 - 문자열 길이만 일치
        if word == "?"*len(word):
            answer.append(front.head.length[len(word)])
            
        # 맨 앞 글자가 ?인 경우는 역방향 트라이를 사용
        elif word[0] == "?":
            prefix = word[::-1].split("?")[0]
            answer.append(back.start_with(prefix, len(word)))
        else:
            prefix = word.split("?")[0]
            answer.append(front.start_with(prefix, len(word)))
    
    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?", "????o", "?????"]
    print(solution(words, queries))