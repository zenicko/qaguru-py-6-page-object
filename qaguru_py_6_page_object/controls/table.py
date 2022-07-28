from selene.core.entity import Element
from selene.support.conditions import have


class Table:
    def __init__(self, element: Element):
        self.element = element

    def row(self, index: int):
        self.row_ = self.element.all("tr")[index]
        return self

    def should_have_exact_texts(self, texts):
        self.row_.all('td').should(have.exact_texts(*texts))
        return self
