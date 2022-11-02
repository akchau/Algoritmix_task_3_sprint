"""id = 73689835."""


class User:
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = tasks
        self.fine = fine

    def __lt__(self, other):
        if int(self.tasks) > int(other.tasks):
            return True
        elif int(self.tasks) == int(other.tasks):
            if int(self.fine) < int(other.fine):
                return True
            elif int(self.fine) == int(other.fine):
                if self.name < other.name:
                    return True
        return False

    def __str__(self):
        return self.name


def quicksort_inplace(array, left, right):
    if left >= right:
        return
    left_idx = left
    right_idx = right

    pivot_idx = (left + right) // 2
    pivot = array[pivot_idx]
    while left_idx < right_idx:
        while array[left_idx].__lt__(pivot):
            left_idx += 1
        while pivot.__lt__(array[right_idx]):
            right_idx -= 1
        if left_idx <= right_idx:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
            left_idx += 1
            right_idx -= 1
    quicksort_inplace(array, left, right_idx)
    quicksort_inplace(array, left_idx, right)


def main():
    user_num = int(input())
    user = [
        User(*input().split()) for _ in range(user_num)
    ]
    quicksort_inplace(user, 0, user_num - 1)
    print(*user, sep='\n')


if __name__ == '__main__':
    main()
