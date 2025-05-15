def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


if __name__ == "__main__":
    # boys = names()
    # girls = names()
    # print(boys("Vasya"))
    # print(boys("Dima"))
    # print(boys("Petya"))
    # print(girls("Masha"))
    # print(girls("Sveta"))
    count = counter()
    print(count(1))
    print(count(1))
    print(count(1))
    print(count(-3))
