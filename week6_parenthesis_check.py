from simple_stack import Stack


def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '(', '['):
            stack.push(ch)
        elif ch in ('}', ')', ']'):
            if stack.is_empty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left != '{') or (ch == ']' and left != '[') or (ch == ')' and left != '('):
                    return False

    return stack.is_empty()


def bracket_counts(statement):
    count = 0
    for ch in statement:
        if ch in ('(', ')', '{', '}', '[', ']'):
            count += 1

    return count


def bracket_result(res1, res2):
    if res1:
        print('OK_{}'.format(res2))
    else:
        print('Wrong_{}'.format(res2))


if __name__ == '__main__':
    sample_str = input()
    # sample_str = ("{ A ((1)abc )}")

    result1 = check_brackets(sample_str)
    result2 = bracket_counts(sample_str)

    bracket_result(result1, result2)