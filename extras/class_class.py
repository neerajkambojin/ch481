class NewList(list):
    def remove_max(self):
        self.remove(max(self))

    def remove_min(self):
        self.remove(min(self))


list1 = [34, 45, 65, 75, 45, 435, 67, 435, 457, 2435, 653, 21]

print(list1)
