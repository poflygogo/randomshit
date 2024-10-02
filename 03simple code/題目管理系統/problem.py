class Problem:
    def __init__(self, des, ans, problem_type='default'):
        self.description = des
        self.answer = ans
        self.type = problem_type

    def __str__(self):
        return f'{self.description}\nans: {self.answer}'

    def __repr__(self):
        return f'Problem(description={self.description}, answer={self.answer})'

    def judge(self, user_answer):
        return user_answer.rstrip() == self.answer

    def problem_type(self):
        return self.type


class Choice(Problem):
    def __init__(self, des, ans, choice, problem_type='choice'):
        super().__init__(des, ans, problem_type)
        self.choice = choice

    def __str__(self):
        return f'{self.description}\n{self.choice}\nans: {self.answer}'

    def __repr__(self):
        return f'Choice(description={self.description}, choice={self.choice}, answer={self.answer})'


class TrueAndFalse(Problem):
    def __init__(self, des, ans, problem_type='TrueAndFalse'):
        super().__init__(des, ans, problem_type)


class MultiChoice(Problem):
    def __init__(self, des, ans, problem_type='MultiChoice'):
        super().__init__(des, ans, problem_type)


if __name__ == '__main__':
    a = Problem('ababa', 'aaaa')
    print(repr(a))
