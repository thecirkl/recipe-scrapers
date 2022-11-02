# mypy: allow-untyped-defs

from ._abstract import AbstractScraper

def get_ingredient_text(e):
    t = ''
    qty = e.find("span", {"class": "Ingredient-quantity"})
    if qty is not None:
        amount = qty['data-quantity'] or ''
        unitname = e.find("span", {"class", 'Ingredient-unitName'})
        unit = None
        if unitname:
            unit = unitname['data-singular-name']
        unit = unit or qty['data-unit'] or ''
        t = (amount + ' ' + unit).strip()
    iname = e.find("span", {"class", "Ingredient-name"})
    if iname is not None:
        itext = iname['data-singular']
        t = t + ' ' + (itext or '')
    return t.strip()

class Tasteline(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteline.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_elements = self.soup.findAll("li", {"class": "Ingredient u-contents"})
        return [
            get_ingredient_text(element) for element in ingredient_elements if element.get_text()
        ]

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
