def typed(type_in):
    def real_decorator(func):
        def wrapper(*args):
            for elem in args:
                if not isinstance(elem, type_in):
                    raise AttributeError(f"Тип должен быть  {type_in}")
            return func(*args)

        return wrapper

    return real_decorator


@typed(int)  # как буд-то @real_decorator
def calculate(a, b, c):
    return a + b + c


@typed(str)
def convert(a, b):
    return a + b


# У тебя есть функция process_data(data: list[int]) -> list[int],
# которая принимает список целых чисел и возвращает новый список,
# где каждый элемент увеличен на 1.
# Теперь твоя задача — написать декоратор skip_negatives, к
# оторый будет перед вызовом process_data удалять все отрицательные числа из списка.


def decorator_parametrize(threshold=None):
    if threshold is None:
        threshold = 0

    def skip_negatives(func):
        def wrapper(data):
            list_digit = [elem for elem in data if elem > threshold]
            return func(list_digit)

        return wrapper

    return skip_negatives


@decorator_parametrize()
def process_data(data: list[int]) -> list[int]:
    return data


if __name__ == "__main__":
    # как работает под капотом
    # calculate = real_decorator(calculate)
    # calculate = typed(int)(calculate)
    # print(calculate(2, 2, 3))
    # print(convert("1", "aasq"))
    print(process_data([-4, 3, 5, 8, -4, -1, 1]))
