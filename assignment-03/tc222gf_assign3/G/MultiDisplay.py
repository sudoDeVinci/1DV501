__author__ = "Tadj Cazaubon"


from dataclasses import dataclass


@dataclass
class MultiDisplay:
    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_count(self, count):
        self.count = count

    def get_count(self):
        return self.count

    def to_string(self):
        return (f"Message: {self.message}, Count: {self.count}")

    def display(self):
        for c in range(self.count):
            print(self.message)

    def set_display(self, message, count):
        self.message = message
        self.count = count
        self.display()


# Print out examples:
md = MultiDisplay()
md.set_message("Hello World!")
md.set_count(3)
print(md.to_string())                  # print-out
md.display()                           # print-out

md.set_display("Goodbye cruel world!", 2)    # print-out
print(md.to_string())                        # print-out
print("Current message:", md.get_message())  # print_out
