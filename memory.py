# implementation of card game - Memory

import simplegui
import random


guesses = []
cards = []
guessed = []

# helper function to initialize globals
def new_game():
    #guesses, cards, guessed zeroed
    #cards = range(8), concat to self.randomize order
    
    pass
    
    
def evaluate_match():
    #if not flipped && not current
        # if guesses.len() = 1, compare
        #    if match, return match, else return false. 
        #if guesses.len() = 0, move on
        #if guesses.len=2, erase guesses
    # else unflip
 pass
    

     
# define event handlers
def mouseclick(pos):
    # which card was clicked. 
    # guesses . append()
    # evaluate-match()
    #if match is true, add cards to list of ignore
    #if guesses.len() < total, you won game
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #draw lines
    
    #draw flipped cards
    
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric