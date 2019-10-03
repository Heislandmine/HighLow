import random


class Dealer:
    def __init__(self):
        # 山札を生成してシャッフル
        self.deck = list(range(1, 14)) * 4
        random.shuffle(self.deck)

    # 山札からカード一枚引く
    def draw_card(self):
        return self.deck.pop()


class Agent:
    def __init__(self, p_type=0):
        # 行動計画を生成　0 = 低い, 1 = 高い, 2 = ランダム
        if p_type == 0:
            self.act_plan = [1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0]
        elif p_type == 1:
            self.act_plan = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        elif p_type == 2:
            self.act_plan = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif p_type == 3:
            self.act_plan = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    def predict(self, open_card):
        plan = self.act_plan[open_card - 1]
        if plan == 2:
            return random.choice([0, 1])

        else:
            return plan


class HighAndLow:
    def __init__(self):
        self.count = 0
        self.dl = None
        self.ag = None

    def open_first_card(self, dl):
        return dl.draw_card()

    def card_comp(self, c_card, n_card):
        if c_card < n_card:
            return 1
        elif c_card > n_card:
            return 0
        else:
            return 2  # 2枚のカードが同じ場合

    def eval(self, p_result, result):
        if p_result == result:
            self.count += 1
            return 0
        else:
            return 1

    def play_game(self, dl, ag, first_card):
        open_card = first_card
        while True:
            predict_result = ag.predict(open_card)
            next_card = dl.draw_card()
            result = self.card_comp(open_card, next_card)

            if result == 2:
                open_card = next_card
            else:
                eval_result = self.eval(predict_result, result)
                if eval_result == 1:
                    break
                else:
                    open_card = next_card

            if len(dl.deck) == 0:
                break

    def high_and_low(self, dl, ag):
        self.dl = dl
        self.ag = ag
        first_card = self.open_first_card(self.dl)
        self.play_game(self.dl, self.ag, first_card)

        return self.count

