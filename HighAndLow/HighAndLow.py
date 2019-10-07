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
        self.predict_num = 0
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
            self.predict_num = random.choice([0, 1])

        else:
            self.predict_num = plan


class HighAndLow:
    def __init__(self):
        self.count = 0
        self.open_card = 0
        self.next_card = 0
        self.result = 0
        self.eval_result = 0
        self.record = []
        self.dl = None
        self.ag = None

    def csv_record(self, ag):
        record = []
        record.append(self.count + 1)
        record.append(self.open_card)
        record.append(self.next_card)
        record.append(ag.predict_num)
        record.append(self.eval_result)
        self.record.append(record.copy())


    def card_comp(self, c_card, n_card):
        if c_card < n_card:
            self.result = 1
        elif c_card > n_card:
            self.result = 0
        else:
            self.result = 2  # 2枚のカードが同じ場合

    def eval(self, p_result, result):
        if p_result == result:
            self.eval_result = 0
        else:
            self.eval_result = 1

    def play_game(self, dl, ag, first_card):
        self.open_card = first_card
        while True:
            ag.predict(self.open_card)
            self.next_card = dl.draw_card()
            self.card_comp(self.open_card, self.next_card)

            if self.result == 2:
                self.eval_result = self.result
                self.csv_record(ag)
                self.open_card = self.next_card
            else:
                self.eval(ag.predict_num, self.result)
                if self.eval_result == 1:
                    self.csv_record(ag)
                    break
                else:
                    self.csv_record(ag)
                    self.open_card = self.next_card

            if len(dl.deck) == 0:
                break

    def high_and_low(self, dl, ag, count):
        self.dl = dl
        self.ag = ag
        self.count = count
        first_card = dl.draw_card()
        self.play_game(self.dl, self.ag, first_card)

        return self.record

