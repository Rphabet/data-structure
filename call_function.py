# 매직 메소드 __call__을 통해 함수를 호출하는 것처럼 클래스의 객체도 호출할 수 있게 만들어보자.

import random


class RandomNumberReturn:
    def __init__(self):
        self.numbers = [n for n in range(1, 101)]

    def pick(self):
        print('1. Before shuffling -->>> ', self.numbers)
        random.shuffle(self.numbers)
        print('2. After shuffling -->>> ', self.numbers)
        return sorted([random.choice(self.numbers) for _ in range(10)])


if __name__ == '__main__':
    randnum = RandomNumberReturn()
    print(randnum.pick())


class RandomNumberReturn:
    def __init__(self):
        self.numbers = [n for n in range(1, 101)]

    def pick(self):
        # print('1. Before shuffling -->>> ', self.numbers)
        random.shuffle(self.numbers)
        # print('2. After shuffling -->>> ', self.numbers)
        return sorted([random.choice(self.numbers) for _ in range(10)])

    def __call__(self):
        print('Special Method __call__ is called!!!!!!!!')
        return self.pick()


if __name__ == '__main__':
    randnum = RandomNumberReturn()
    print(randnum)
    print(randnum())

    # print(randnum.pick())

    print(callable(randnum))


