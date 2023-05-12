import settings


def validate_title_importance(title_importance):
    try:
        new_title_importance = int(title_importance-1)
        return max(0, min(5, new_title_importance))
    except:
        return 5


class Heading:
    def __init__(self, title_importance, text):
        self.title_importance = validate_title_importance(title_importance)
        self.text = text

        self.markdown = f'\n{settings.TITLE_IMPORTANCE[self.title_importance]} {self.text}\n'
