"""id = 73678425."""


class User:
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = tasks
        self.fine = fine

    def __lt__(self, other):
        if int(self.tasks) > int(other.tasks):
            return True
        if int(self.tasks) < int(other.tasks):
            return False
        if int(self.tasks) == int(other.tasks):
            if int(self.fine) > int(other.fine):
                return False
            if int(self.fine) == int(other.fine):
                if self.name > other.name:
                    return False
                if self.name == other.name:
                    return False
                if self.name < other.name:
                    return True
            if int(self.fine) < int(other.fine):
                return True

    def __str__(self):
        return self.name


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j].__lt__(pivot):
            i += 1
            array[i], array[j], = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def quicksort_inplace(a, low=0, high=None):
    if high is None:
        high = len(a)-1
    if low < high:
        pivot_index = partition(a, low, high)
        quicksort_inplace(a, low, pivot_index - 1)
        quicksort_inplace(a, pivot_index + 1, high)


if __name__ == "__main__":
    user_num = int(input())
    user = [
        User(*input().split()) for _ in range(user_num)
    ]
    quicksort_inplace(user)
    i = 0
    print(*user, sep='\n')
