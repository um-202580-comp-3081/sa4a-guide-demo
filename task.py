class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "O"
        return f"{status} {self.title}"
