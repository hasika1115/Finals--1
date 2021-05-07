#Import all modules
import turtle as trtl
import time as time
import random as rand


# Background color and screen size
wn = trtl.Screen()
wn.bgcolor("light blue")
wn.setup(width=1.0, height=1.0, startx=None, starty=None)

# Set turtle position
trtl.penup()
trtl.setposition(-140, 100)
trtl.hideturtle()

# Font type and size
font_setup = ("Verdana", 20, "normal")
font_setup_title = ("Verdana", 20, "normal")


# Create images
backpack_img = "backpack.gif"
boys_img = "argue.gif"
envelope_img = "envelope.gif"
candy_img = "candy.gif"
person_img = "person.gif"
best_friend_img = "best_friend.gif"
friend_1_img = "friend_1.gif"
friend_2_img = "friend_2.gif"
friend_1_letter_img = "friend_1_letter.gif"
friend_2_letter_img = "friend_2_letter.gif"

#Function definitions
#Used to display the note prompt on the screen
def display_prompt(title, msg):
    note = trtl.textinput(title, msg)
    return note


#Used to allow any words to be entered with preferred color, coordinates, and font size
def display_msg(color, note, x, y, font_size):
    trtl.penup()
    trtl.setposition(x, y)
    trtl.pencolor(color)
    trtl.write(note, font=("Verdana", font_size, "normal"))


# Draw shape and animate for any image
def draw_and_animate(x, y, img):
    img_trtl = trtl.Turtle()
    img_trtl.penup()
    img_trtl.setposition(x, y)
    img_trtl.shape(img)
    img_trtl.right(90)
    time.sleep(0.1)
    img_trtl.forward(175)
    wn.update()


#Wait (similar to a sleep, allows for user input)
def wait():
    input('Press enter to continue\n')


#Paint any image on the screen at a set position
def paint_image(img_name, x, y):
    paint_trtl = trtl.Turtle()
    paint_trtl.penup()
    paint_trtl.shape(img_name)
    paint_trtl.setposition(x, y)
    wn.update()


#Displays the note on the screen that the user wrote in the note prompts (Sequencing)
def draw_note_path():

    #Take user note input for each back pack
    first_note = display_prompt("Backpack 1", "Write a message.")
    print("This is the note you wrote: " + first_note)
    
    #if the length of the note is greater than 10 characters, take first 10 chars and add ... to show some characters are ommited
    if len(first_note) > 10:
        first_note = first_note[0:10] + '...'

    #Display the note on screen
    display_msg('red', first_note, -50, 50, 10)

    #Take user note input for each back pack
    second_note = display_prompt("Backpack 2", "Write a message.")
    print("This is the note you wrote: " + second_note)

    #if the length of the note is greater than 10 characters, take first 10 chars and add ... to show some characters are ommited (Selection)
    if len(second_note) > 10:
        second_note = second_note[0:10] + '...'

    #Display the note on screen
    display_msg('blue', second_note, 100, 50, 10)

    #Add envelope image to window
    wn.addshape(envelope_img)

    #Animate envelope, for i in range loop, each iteration it takes the value from the range and pass to the function (Iteration)
    for i in [-100, 175]:
        draw_and_animate(i, 200, envelope_img)

    #clear to animate the text
    input("Press enter to switch the backpacks")
    trtl.clear()

    #Animate to show the switch of backpack occured by switching the notes displayed
    display_msg('red', second_note, -50, 50, 10)
    display_msg('blue', first_note, 100, 50, 10)

    print("The backpacks have been switched!")
    wait()
    wn.clear()
    trtl.hideturtle()

    # Make the screen aware of the new files
    wn.addshape(friend_1_letter_img)
    wn.addshape(friend_2_letter_img)
    wn.tracer(False)

    paint_image(friend_1_letter_img, -130, -50)
    paint_image(friend_2_letter_img, 100, -50)

    print(
        "Because you decided to write a note, the boys discover these notes later in the day, and realize their mistakes."
    )
    wait()
    wn.clear()
    #Display iamge
    paint_image(best_friend_img, 0, 0)
    #Display note
    display_msg('red', "Your note helped!!", -100, 100, 15)
    #Display note, Used string manipulation to add names
    display_msg(
        'red',
        greeting_name.capitalize() + ", " + first_person.capitalize() +
        " and " + second_person.capitalize() + " are best friends again!", -250,
        75, 15)
    display_msg('red', "Click on the screen to celebrate !!", -175, -100, 15)
    trtl.hideturtle()


#Animate the candy to come into the backpacks.
def draw_candy_path(color):

    #Add envelope image to window
    wn.addshape(candy_img)

    #Animate Candy, Similar to draw_note_path function for loop, Instead this is while loop and increment the i value after calling function
    i = -100
    while i < 400:
        draw_and_animate(i, 200, candy_img)
        i += 290

    trtl.penup()

    #Display the outcome
    display_msg(color, "It's a good gesture but won't help!! Click to quit.",
                -250, 100, 15)


#Clear the screen and shut down the window
def quit(x, y):
    wn.clear()
    wn.bye()


#Fireworks to celebrate if they get to the end of the story
def fireworks(x, y):
    wn.clear()
    wn.bgcolor("black")
    screen = trtl.Screen()
    screen.bgcolor("black")

    # Different colors for fireworks
    color = [
        "red", "orange", "yellow", "green", "blue", "purple", "turquoise",
        "fuchsia"
    ]

    # Different message each time
    congrats = ["Congratulations!", "You did it!", "You Succeeded!", "Nice Job!"]
    trtl.speed(100)
    trtl.color("red")

    #Loop to display 15 fireworks in different positions randomly
    i=0
    while (i<15):
      j=0
      x = rand.randint(-250, 250)
      y = rand.randint(-200, 200)
      trtl.penup()
      trtl.goto(x, y)
      trtl.pendown()
      trtl.pencolor(rand.choice(color))        
      size = rand.randint(30, 125)
      while (j<36):
        #Loop draw 36 lines that shows like a firework
        trtl.forward(size)
        trtl.backward(size)
        trtl.left(10)
        j+=1
      
      #Increment the variable i so that it increases each time the loop is run  
      i+=1

    #Writing on screen
    trtl.penup()

    #Display randowm message each time
    display_msg('white', rand.choice(congrats), -200, 0, 30)
    trtl.hideturtle()
    wn.listen()
    wn.onclick(quit)



# Main body starts here
#Title (Prints on the screen)
trtl.write("The Backpack Switch", font=font_setup_title)

#Wait for 1 seconds
time.sleep(1)

#Ask user for name and print intro
#greeting_name = input("Enter your name: ")

greeting_name = input("Please enter your name: ")


# Check if there's a number in the name
while (greeting_name=='' or greeting_name.isnumeric() == True):
  greeting_name = input("Please enter a valid name: ")



#name =trtl.textinput("Name", "Enter your name")
trtl.penup()
trtl.setposition(-75, 50)

#String concatenation
display_msg('green', "Hello " + greeting_name.capitalize() + "!", -100, 50, 20)
time.sleep(1)
display_msg('black', "Welcome to this interactive story.", -225, 0, 20)
time.sleep(1)
display_msg('black', "Look at the console for the story.", -225, -50, 20)

#Wait for user to continue, and clear screen for story
wait()
wn.clear()

# Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# Make the screen aware of the new files
wn.addshape(friend_1_img)
wn.addshape(friend_2_img)
wn.tracer(False)

first_person = input("Enter First Friend Name : ")
print("\n")

# Check if there's a number in the name
while (first_person =='' or first_person.isnumeric() == True):
  first_person = input("Please enter a valid name: ")

paint_image(friend_1_img, -135, 0)
display_msg('blue', first_person, -150, 125, 10)
trtl.hideturtle()

second_person = input("Enter Second Friend Name : ")
print("\n")

# Check if there's a number in the name
while (second_person =='' or second_person.isnumeric() == True):
  second_person = input("Please enter a valid name: ")

paint_image(friend_2_img, 50, 0)
display_msg('blue', second_person, 80, 125, 10)
trtl.hideturtle()

## Describe the wait here
wait()
wn.clear()

# Make the screen aware of the new files
wn.addshape(boys_img)
wn.addshape(person_img)
wn.addshape(best_friend_img)
wn.tracer(False)

#-----function calls-----
paint_image(boys_img, -135, 0)
paint_image(person_img, 160, -50)

display_msg('blue', "Hmm... ", 80, 50, 10)
print("\n")

friends_names = first_person +' and ' + second_person

print(
  friends_names + " used to be best friends, but then they encountered a slight problem, and now aren't friends. Your job is to make them friends before the end of the school day.\n"
)
wait()
print(
  "The one thing that works in your favor is that they have similar backpacks.\n"
)

## Describe the wait here
wait()
wn.clear()

#Add image to to window
wn.addshape(backpack_img)

# Function call to display image on screen
trtl.hideturtle()
display_msg(
  'purple', first_person.capitalize() + ' and ' +
  second_person.capitalize() + "'s Backpacks " , -125, 100, 15)

# Function call to add images at position specified
paint_image(backpack_img, -100, 0)
paint_image(backpack_img, 175, 0)
paint_image(person_img, 50, -150)
trtl.penup()

print("You have two options.\n")
print("A: Just switch the backpacks.\n")
print(
  "B: You can slip a note into their backpacks, writing something good about the other person and switch their backpacks.\n"
)

choice = input("What do you do? Choose A or B : ")
trtl.clear()

# Results of each choice
while (choice.lower() !='a' and choice.lower() !='b') :
  choice = input("Choose A or B : ")

#String manipulation
#choice = choice.lower()

if choice.lower() == "a":
  print("Just switching the backpacks could cause more damage! \n")
  print("It might be better to do something nice to help them get along. \n")
  print("Do you wish to add something? \n")
  choice = input("Choose Yes or No : ")

  #Used upper function to compare user input
  if choice.upper() == "YES" or choice.upper() == 'Y':
      print("\nYou have two option \nA: Drop a candy \n")
      print("B: Drop a note \n")
      choice = input("What do you do? Choose A or B: ")
      
      if choice.upper() == "B":
          draw_note_path()
          wn.listen()
          wn.onclick(fireworks)
      elif choice.upper() == "A":
          print(
              "Dropping a candy may not help as they both get candy and don't know who it's from\n"
          )
          draw_candy_path("violet")
          wn.listen()
          wn.onclick(quit)
  elif choice.upper() == "NO" or choice.upper() == 'N':
      print(" \n")
      wn.clear()
      print(
          "Since you switched the backpacks and didn't add anything, the boys become even more mad at each other. This causes them to never become friends. Try again!"
      )
      display_msg('red', "You chose not to add, Click to exit.", -240, 0, 20)
      trtl.hideturtle()
      wn.onclick(quit)
  else:
      print("Not a right Option \n")
      wn.clear()
      display_msg('red', "You have selected invalid option, Click to exit.",
                  -250, 0, 15)
      wn.onclick(quit)
elif choice.lower() == "b":
  print("Type what you want to write on the note in the box on the screen")
  draw_note_path()

  wn.listen()
  wn.onclick(fireworks)

else:
    trtl.hideturtle()
    wn.clear()
    print("You must answer A or B. Click to exit.")
    display_msg('black', "Click to exit the program.", -175, 0, 20)
    trtl.hideturtle()
    wn.listen()
    wn.onclick(quit)