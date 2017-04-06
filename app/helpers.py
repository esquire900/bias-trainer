class Anchoring:
    cnt = False

    def __init__(self, user, cnt):
        self.user = user
        self.cnt = cnt

    def get_user_stage(self):
        if self.cnt < 10:
            return 0
        if 10 < self.cnt < 20:
            return 1
        if 20 < self.cnt < 30:
            return 2
        if self.cnt > 30:
            return 3

    def get_display_explanation(self):
        if self.cnt == 0:
            return 'start'
        if self.cnt == 10:
            return 'explanation'
        if self.cnt == 20:
            return 2
        return False
