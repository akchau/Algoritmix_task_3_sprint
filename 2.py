"""id = 73775017."""


class User:
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = tasks
        self.fine = fine

    def __lt__(self, other):
        self_t = (self.tasks, self.fine, self.name)
        other_t = (other.tasks, other.fine, other.name)
        return self_t < other_t

    def __str__(self):
        return self.name


def quicksort(array, left, right):
    if left >= right:
        return
    left_idx = left
    right_idx = right
    pivot = array[(left+right)//2]
    while left_idx < right_idx:
        while array[left_idx] < pivot:
            left_idx += 1
        while pivot < array[right_idx]:
            right_idx -= 1
        if left_idx <= right_idx:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
            left_idx += 1
            right_idx -= 1
    quicksort(array, left, right_idx)
    quicksort(array, left_idx, right)


def transformation(user_0, user_1, user_2):
    user_1 = - int(user_1)
    user_2 = int(user_2)
    return [user_0, user_1, user_2]


def main():
    user_num = int(input())
    user = [
        User(*transformation(*input().split())) for _ in range(user_num)
    ]
    quicksort(user, 0, user_num - 1)
    print(*user, sep='\n')


if __name__ == '__main__':
    main()
