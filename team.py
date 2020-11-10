class Team:
    """Команда-участник"""
    name = ''
    count_points = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
