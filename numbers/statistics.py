
def mean(numbers):
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Return the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def mode(numbers):
    """Return the mode of a list of numbers."""
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes

def standard_deviation(numbers):
    """Return the standard deviation of a list of numbers."""
    m = mean(numbers)
    variance = sum([(num - m) ** 2 for num in numbers]) / len(numbers)
    return variance ** 0.5
