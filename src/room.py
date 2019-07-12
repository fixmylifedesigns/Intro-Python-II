# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (self, name, description, items=[]):
        self.name = name 
        self.description = description
        self.items = items
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.n_to = None

    # def __str__(self):
    #     return f"{self.name}"

    def __str__(self):
        item_names = [item.name for item in self.items]
        put = ", ".join(item_names)
        return (f"{self.name}"
                f"\n {self.description}"
                f"\n Items in this area: {put}"
                    )

    # def add_item

    # def add_item(self, item):
    #     self.items.append(item)
    #     # self.location.remove(item)

    # def remove_item(self, item):
    #     self.items.remove(item)
    #     # self..append(item)
