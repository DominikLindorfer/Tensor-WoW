#-----Find WA Position on Screen (click on anchor in the middle)-----
from pynput import mouse    
from pynput import keyboard
from pynput.keyboard import Key
from threading import Thread

def on_move(x, y):
    # Label_WAPosition["text"] = 'Pointer moved to {0}'.format((x, y))
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        # Stop listener
        return False

# def on_click(x, y, button, pressed):
#     btn = button.name

#     if btn == 'left':
#         print('Left if Pressed')
#         # ====== < Handle Pressed or released Event ====== > # 
#         if pressed:
#             print('Do somethin when Pressed with LEft')
#         else:
#             print('LEFT is Released')
#     elif btn == 'right':
#         print('Right BTN was pressed ')
#         # ====== < Handle Pressed or released Event ====== > # 
#         if not pressed:
#             print('right Button is released')
#         else:
#             pass

#working below!
# def on_click(x, y, button, pressed):
#     print(button)  # Print button to see which button of mouse was pressed
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
    
# listener = mouse.Listener(on_click=on_click)
# listener.start()
# listener.stop()

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1s}'.format('down' if dy < 0 else 'up',(x, y)))

# Collect events until released
def find_mouseposition():
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
        
def thread_findmouse():
    t = Thread(target = find_mouseposition)
    t.start()