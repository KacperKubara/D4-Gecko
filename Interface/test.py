
array = [1, 2, 3, 4]


def foo(value):
    try:
        try:
            return int(value)
        except ValueError:
            print('Value error')
            return float(value)
    except ValueError: #id could not convert string to float
        temp = list(value)
        for i, element in enumerate(temp):
            try:
                if element is not '.':
                    int(element)
            except Exception as e:
                temp[i] = '0'
        return (float("".join(temp)))


print(foo('17'))

