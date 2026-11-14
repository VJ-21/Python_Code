class Parent:
    def __init__(self):
        self.name = "Parent లోని పేరు"

    def get_name(self):   # 👉 ఒక method ద్వారా access చేయించండి
        return self.name

class Child(Parent):
    def __init__(self):
        super().__init__()         # Parent constructor call
        self.name = "Child లోని పేరు"  # Override

    def show_parent_name(self):
        print("Parent name:", super().get_name())  # ✅ ఇప్పుడు పని చేస్తుంది

c = Child()
print("Child name:", c.name)
c.show_parent_name()
