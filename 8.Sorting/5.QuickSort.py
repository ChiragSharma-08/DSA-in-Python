def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]

    smaller = []
    bigger = []

    for number in numbers[:-1]:
        if number <= pivot:
            smaller.append(number)
        else:
            bigger.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)

prices = [850 , 200, 520, 100, 430]
print(quick_sort(prices))