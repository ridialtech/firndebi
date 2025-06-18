class Diploma:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @property
    def is_recent(self):
        return self.year >= 2024

def test_is_recent_true():
    d = Diploma("Licence", 2025)
    assert d.is_recent is True

def test_is_recent_false():
    d = Diploma("Licence", 2019)
    assert d.is_recent is False
