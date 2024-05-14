from psychopy import visual, core, event

# Create a window
win = visual.Window([800, 600], fullscr=False, monitor="testMonitor", units="pix", color=(1, 1, 1))

# Define the text stimulus.
# We test the following hindi fonts: Arial Unicode MS, Arial, Mangal, Sahadeva, Lohit Devanagari.
text = visual.TextStim(win, text=u'नमस्ते दुनिया', font='Arial Unicode MS', height=40, wrapWidth=700, pos=(0,0), color=(0,0,0))

# Loop until a specific key is pressed
while True:
    # Draw the text to the window
    text.draw()

    # Flip the window
    win.flip()

    # Check for key presses
    keys = event.getKeys()
    if 'space' in keys:  # If the space bar is pressed
        break  # Exit the loop

# Close the window
win.close()
core.quit()