import turtle
import pandas
from answer import AnswerBoard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/ 50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    elif answer_state in state_list:
        guessed_states.append(answer_state)
        # index = data[data.state == answer_state].index[0]
        # new_goto = (data["x"][index], data["y"][index])
        state_data = data[data.state == answer_state]
        new_goto = (int(state_data.x), int(state_data.y))
        AnswerBoard(new_goto, answer_state)

# # How to get x,y
# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# states_to_learn.csv
# states_to_learn = []
# for state in state_list:
#     if state not in guessed_states:
#         states_to_learn.append(state)

states_to_learn = [state for state in state_list if state not in guessed_states]

# data_dict = {
#     "states_to_learn": states_to_learn
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("states_to_learn.csv")
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
