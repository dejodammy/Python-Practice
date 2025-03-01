import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. STATE GAME")
image = r"F:\DEJO\Documentos\Python_Course\us_state_game\us\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"F:\DEJO\Documentos\Python_Course\us_state_game\us\50_states.csv")
state = data['state'].str.lower()
states = state.to_list()


score = 0
play_on = True
correct_answers = []
while play_on:    
    state_answer = screen.textinput(f"Guess state score:{score}/50" , "Guess a state").lower().strip()
    
    if state_answer == "exit":
        missed_states = [s for s in states if s not in correct_answers]
        
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missedstate.csv")
        break
    
    if state_answer in states:
        score = score + 1
        state_data = data[data['state'].str.lower() == state_answer]
        x = int(state_data['x'].iloc[0])  # Get the x coordinate
        y = int(state_data['y'].iloc[0])  # Get the y coordinate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x,y)
        t.write(state_answer)
        states.remove(state_answer)
        correct_answers.append(state_answer)
        

turtle.mainloop()


