from simple_stack import Stack


def check_brackets(statement):
    """
    조건1: 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야함
    조건2: 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
    조건3: 괄호 사이에는 포함 관계만 존재함s

    :return:
    """
    stack = Stack()

    for ch in statement:  # 문자열의 각 문자 character에 대해...
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.is_empty():
                return False  # 조건2 위반
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
                    return False  # 조건3 위반

    return stack.is_empty()  # False면, 조건 1위반


if __name__ == '__main__':
    test_str = ("{A[(i+1)] = 0; }", "if( (i==0) && (j==0 )", "A[ (i+1] ) = 0;")
    for s in test_str:
        m = check_brackets(s)
        print(s, " ---> ", m)