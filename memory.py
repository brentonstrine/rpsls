# implementation of card game - Memory

import simplegui
import random


guesses = []
cards = range(16)
flipped = {}

# helper function to initialize globals
def new_game():
    global guesses, cards, flipped
    guesses = []
    flipped = {}
    cards = range(8) + range(8)
    random.shuffle(cards)
    print cards
    
    #guesses, cards, guessed zeroed
    #cards = range(8), concat to self.randomize order
    
    pass
    
    
def evaluate_match():
        global guesses, cards
        #if not flipped && not current 
        #if guesses.len() = 1, move on
        print "guesses: ", guesses
        if(len(guesses)==1):
            # if guesses.len() = 2, compare
            print len(guesses)
            return False
        elif(len(guesses)==2):
            if(cards[guesses[0]]==cards[guesses[1]]):
                return True
            else:
                return False
        #if guesses.len=3, erase guesses
        elif(len(guesses)==3):
            guesses = [guesses[2]]
#            add first to guesses
        #elif(len(guesses)==3):
        #    guesses = []
    # else unflip


     
# define event handlers
def mouseclick(pos):
    global flipped, guesses
    # which card was clicked. 
    guess = pos[0] / 50
    
    #print guesses
    # guesses . append()
    guesses.append(guess)
    #print guesses
    # evaluate-match()
    if(evaluate_match()):
        #add guessed cards to permanent flip
        print flipped
        print guesses[0]
        flipped[guesses[0]] = True
        flipped[guesses[1]] = True
        print flipped
    else:
        print "evaluates false"
        
    #if match is true, add cards to list of ignore
    #if guesses.len() < total, you won game
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global guesses, cards
    #draw lines
    
    #draw guessed cards
    for idx in guesses:
        posS = idx * 50
        posE = posS + 50
        topright = [posS, 0]
        topleft = [posE, 0]
        bottomright = [posS, 100]
        bottomleft = [posE, 100]
        num = str(cards[idx])        
        canvas.draw_polygon([topleft, topright, bottomright, bottomleft], 1, "#fff", "#fcd")
        canvas.draw_text(num,[posS + 18, 60], 30, "#000")

    
    #draw flipped cards
    for idx in flipped:
        posS = idx * 50
        posE = posS + 50
        topright = [posS, 0]
        topleft = [posE, 0]
        bottomright = [posS, 100]
        bottomleft = [posE, 100]
        num = str(cards[idx])        
        canvas.draw_polygon([topleft, topright, bottomright, bottomleft], 1, "#fff", "#afd")
        canvas.draw_text(num,[posS + 15, 60], 30, "#000")


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
