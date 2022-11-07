import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, num):

        if num > len(self.contents):
            return self.contents

        popped_balls = []
        for _ in range(num):
            n = random.randrange(0, len(self.contents))
            popped_balls.append(self.contents.pop(n))

        return popped_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)

        expected_balls_list = []

        for k, v in expected_balls.items():
            for _ in range(v):
                expected_balls_list.append(k)

        try:
            for ball in expected_balls_list:
                balls.remove(ball)
        except:
            pass
        else:
            M += 1

    return round(M / num_experiments, 3)
