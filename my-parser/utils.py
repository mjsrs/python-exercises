import re


class TextParser:
    """Replace words in text

    :param obj: iterable object
    :param replacements: list of tuples with words to replace
        and replacements, ex. [('dog', 'puppy')]
    """

    __slots__ = ['obj', 'replacements']

    def __init__(self, obj, replacements):
        self.obj = obj
        self.replacements = replacements

    def __iter__(self):
        return self

    def next(self):
        return reduce(lambda str, words:
                      self.parse(str, words[0], words[1]),
                      self.replacements, self.obj.next()
                      )

    def parse(self, str, old, new):
        try:
            return re.sub(old, new, str)
        except TypeError:
            return str
