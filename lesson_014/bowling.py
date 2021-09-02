import random

class OddError(Exception):
    pass

class ManyError(Exception):
    pass


class Bowl:

    def __init__(self):
        self.game_result = ""
        self.skittle = 10
        self.result_sum = 0

    def get_result(self):
        skittles = random.randint(0, 10)
        if skittles == 0:
            return "/"
        elif skittles == 10:
            return "X"
        else:
            return str(skittles)


    def get_game_result(self):
        for frame in range(1, 11):
            self.game_result += self.get_result() + self.get_result()
        return self.game_result

    def get_score(self):
        try:
            if len(self.game_result) % 2 != 0:
                raise OddError("Нечетное количество бросков")
            score = list()
            score.append(self.game_result[i:i+2] for i in range(0, len(self.game_result), 2))
            for result in score:
                summ = 0
                for skittle1 in result:
                    if skittle1 == "/":
                        summ += 0
                    elif skittle1 == "X":
                        summ += 10
                    else:
                        summ += int(skittle1)
                if summ > self.skittle:
                    raise ManyError("Сбил больше, чем есть")
                self.result_sum += summ
            return self.result_sum
        except Exception as ex:
            return ex

if __name__=="__main__":
    bow = Bowl()
    bow.get_game_result()
    bow.get_score()

