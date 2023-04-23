"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class MyFac:

    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start = args[0]
                self.stop = args[1]
                self.step = args[2]

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            result = 1
            for i in range(2, self.start + 1):
                result *= i
            self.start += self.step
            return result
        raise StopIteration


f = MyFac(0, 5, 1)
for num in f:
    print(num)
