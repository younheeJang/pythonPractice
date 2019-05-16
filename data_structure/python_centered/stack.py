class Stack:
    #스택 초기화하기 리스트 구현을 위해 자료구조 사용한다
    def __init__(self):
        self.stack = []

    #요소 집어넣기
    def add(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        return False

    #맨 나중에 들어간 요소 꺼내기
    def peek(self):
        return self.stack[-1]

    #팝 메서드로 요소 제거하는 함수 만들기
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        return self.stack.pop()
    #스택 요소 확인 위한 프린트 함수:오브젝트인 요소에 접근할 수 있도록 함.
    def printStack(self):
        for value in self.stack:
            print(value)

#스택 생성
aStack = Stack()

#애드
aStack.add("curious")
aStack.add("jeager")

#프린트
aStack.printStack()
print()

#맨 마지막 값 꺼내보기
print(aStack.peek())
print()

#지우기
aStack.printStack()
aStack.remove()

#확인하기
print()
aStack.printStack()
