import settings


def validate_title_importance(title_importance):
    try:
        new_title_importance = int(title_importance-1)
        return max(0, min(5, new_title_importance))
    except:
        return 5


class Text:
    def __init__(self, title_importance, text):
        self.title_importance = validate_title_importance(title_importance)
        self.text = text

        self.markdown = f'\n{settings.TITLE_IMPORTANCE[self.title_importance]} {self.text}\n'


class CheckButton:
    def __init__(self, text, is_selected=False):
        self.text = text
        self.is_selected = is_selected

    def selected(self):
        self.is_selected = True

    def not_selected(self):
        self.is_selected = False
