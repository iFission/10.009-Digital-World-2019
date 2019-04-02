#%%
'cohort 1'

from libdw import sm


class CM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        if state == 0:
            if inp == 50:
                next_state = 1
                output = (50, '--', 0)
            elif inp == 100:
                next_state = 0
                output = (0, 'coke', 0)
            else:
                next_state = 0
                output = (0, '--', inp)
        elif state == 1:
            if inp == 50:
                next_state = 0
                output = (0, 'coke', 0)
            elif inp == 100:
                next_state = 0
                output = (0, 'coke', 50)
            else:
                next_state = 0
                output = (50, '--', inp)

        return next_state, output


#%%
'cohort 2'

from libdw import sm


class SimpleAccount(sm.SM):
    def __init__(self, initial):
        self.start_state = initial

    # start_state = self.start_state
    def get_next_values(self, state, inp):
        if state < 100 and inp < 0:
            next_state = state + inp - 5
            output = state + inp - 5
        else:
            next_state = state + inp
            output = state + inp

        return next_state, output


#%%
'hw1'

from libdw import sm


class CommentsSM(sm.SM):
    start_state = 'code'

    def get_next_values(self, state, inp):
        if state == 'code':
            if inp == '#':
                next_state = 'comment'
                output = inp
            else:
                next_state = 'code'
                output = None
        elif state == 'comment':
            if inp == '\n':
                next_state = 'code'
                output = None
            else:
                next_state = 'comment'
                output = inp
        return next_state, output


str = "def f(x):  # comment\n return 1"

#%%
'hw2'

from libdw import sm


class FirstWordSM(sm.SM):
    start_state = 'newline'

    def get_next_values(self, state, inp):
        if state == 'newline':
            if inp == ' ':
                next_state = 'newline'
                output = None
            elif inp == '\n':
                next_state = 'newline'
                output = None
            else:
                next_state = 'not newline'
                output = inp
        elif state == 'not newline':
            if inp == '\n':
                next_state = 'newline'
                output = None
            elif inp == ' ':
                next_state = 'done word'
                output = None
            else:
                next_state = 'not newline'
                output = inp
        elif state == 'done word':
            if inp == '\n':
                next_state = 'newline'
                output = None
            else:
                next_state = 'done word'
                output = None
        return next_state, output