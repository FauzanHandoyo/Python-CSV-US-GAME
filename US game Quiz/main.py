import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S Game State")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
state_guessed = []

while len(state_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(state_guessed)} Guess The State!", 
                                    prompt="What is the state?").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in state_guessed]
        break

    if answer_state in all_states and answer_state not in state_guessed: #if the state not input already
        state_guessed.append(answer_state)
        trtl = turtle.Turtle()
        trtl.hideturtle()
        trtl.penup()
        state_data = data[data.state == answer_state]
        trtl.goto(int(state_data.x), int(state_data.y))
        trtl.write(answer_state)

turtle.exitonclick()
