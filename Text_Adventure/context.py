import curses
import time

RECURSION_LIMIT = 0
NAME = ""
TITLE = ""
STORY, PROGRAM = "Story", "Program"
CREDIT = {
    STORY: "",
    PROGRAM: ""
}
MENU = "menu"
OPTIONS = "options"
PROMPT = "prompt"
SCREEN = "screen"
POS = "position"
TEXT = "text"
CALLBACK = "callback"
ENTER_NAME_FORMAT = "Please Enter Your Name with KeyBoard | Key: {:>5}"
STATUS_FORMAT = " Press Up/Down to Control | Press Enter to Select | Press ESC to Leave | Key: {:>5} | Active: {:>2}"

def create_menu_item(pos:int, text: str, callback: callable) -> dict:
    menu_item = { POS: pos, TEXT: text, CALLBACK: callback }
    return menu_item

def init() -> dict:
    context = {}
    context[SCREEN] = curses.initscr()
    context[SCREEN].clear()
    context[SCREEN].keypad(1)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

    return context

def draw_menu(ctx: dict, menu: dict) -> None:
    scr = ctx[SCREEN]
    prompt = menu[PROMPT]
    options = menu[OPTIONS]
    options.sort(key = lambda x: x[POS])
    key = 0
    active = 0
    curses.noecho()

    # Event loop. Listens for key presses from the user
    while(key != 27 and key != 113):

        # Later insert key actions
        if  ( key == 456 or key == 115 or key == curses.KEY_DOWN): active = (active + 1) % len(options)
        elif( key == 450 or key == 119 or key == curses.KEY_UP): active = (active - 1) % len(options)
        elif( key == 10  or key == 101 ): return options[active][CALLBACK]
            
        # Clear Screen
        scr.clear()
        h, w = scr.getmaxyx()

        # Add Title
        scr.attron(curses.color_pair(4))
        scr.addstr(1, 0, ' ' * (w-1))
        scr.addstr(1, 2, TITLE + " - " + NAME)
        scr.attroff(curses.color_pair(4))

        # Add text prompt
        scr.addstr(2, 4, prompt)
        
        # Draw Menu Here
        for idx, option in enumerate(options):
            if(idx == active):
                scr.attron(curses.color_pair(3))
                scr.addstr(8 + idx, 8, option[TEXT])
                scr.attroff(curses.color_pair(3))
            else: scr.addstr(8 + idx, 8, option[TEXT])

        # Draw Status Bar
        status_string = STATUS_FORMAT.format(key, active+1)
        scr.attron(curses.color_pair(4))
        scr.addstr(h-1, 0, ' ' * (w-1))
        scr.addstr(h-1, 0, status_string)
        scr.attroff(curses.color_pair(4))
        scr.move(h-1,w-2)
        scr.refresh()

        # Get Next Key
        key = scr.getch()

def play_too_long(ctx) -> None:
    scr = ctx[SCREEN]
    scr.clear()
    key = 0
    active = 0
    h, w = scr.getmaxyx()
    curses.noecho()

    scr.attron(curses.color_pair(4))
    scr.addstr(1, 0, ' ' * (w-1))
    scr.addstr(1, 2, TITLE)
    scr.attroff(curses.color_pair(4))
    
    scr.attron(curses.color_pair(2))
    scr.addstr(3, 8, "You have been playing for too long!!!")
    scr.addstr(4, 8, "But thanks for the participation in \"" + TITLE + "\".")
    scr.attroff(curses.color_pair(2))
    scr.addstr(6, 8, "Credit:")
    scr.addstr(7, 12, STORY + ": " + CREDIT[STORY])
    scr.addstr(8, 12, PROGRAM + ": " + CREDIT[PROGRAM])
    scr.addstr(9, 8, "Press any key to exit the game...")
    
    status_string = STATUS_FORMAT.format(key, active+1)
    scr.attron(curses.color_pair(4))
    scr.addstr(h-1, 0, ' ' * (w-1))
    scr.addstr(h-1, 0, status_string)
    scr.attroff(curses.color_pair(4))
    scr.move(h-1,w-2)
    scr.refresh()
    # Get Next Key
    key = scr.getch()

def enter_name(ctx) -> str:
    scr = ctx[SCREEN]
    scr.clear()
    key = 0
    h, w = scr.getmaxyx()
    name = ""
    curses.noecho()
    while((key != 10 or len(name) == 0) and key != 27):
        scr.clear()
        scr.attron(curses.color_pair(4))
        scr.addstr(1, 0, ' ' * (w-1))
        scr.addstr(1, 2, TITLE)
        scr.attroff(curses.color_pair(4))
        enter_name_string = ENTER_NAME_FORMAT.format(key)
        scr.attron(curses.color_pair(4))
        scr.addstr(h-1, 0, ' ' * (w-1))
        scr.addstr(h-1, 0, enter_name_string)
        scr.attroff(curses.color_pair(4))

        if(len(name) > 20):
            scr.addstr(3, 8, "You have a name too long...")
            scr.addstr(4, 8, "Mind if you re-enter your name?")
            scr.addstr(5, 8, "Press Enter to continue...")
            while(key != 10 and key != 27):
                key = scr.getch()
            if( key != 27 ): key = 0
            else: break
            name = ""
            continue
        elif(key == 10):
            scr.addstr(3, 8, "Your name cannot be empty...")
            scr.addstr(4, 8, "Mind if you enter your name?")
            scr.addstr(5, 8, "Press Enter to continue...")
            key = 0
            while(key != 10 and key != 27):
                key = scr.getch()
            if( key != 27 ): key = 0
            else: break
            continue
        else:
            scr.addstr(3, 8, "Please enter your name Below: ")
            scr.addstr(4, 12, "Name: {}".format(name))
            scr.attron(curses.color_pair(3))
            scr.addstr(4, 12 + 6 + len(name), " ")
            scr.attroff(curses.color_pair(3))
            scr.addstr(5, 8, "Press enter to comfirm...")
        scr.move(h-1,w-2)
        scr.refresh()
        # Get Next Key
        key = scr.getch()
        if( (key >= 97 and key <= 122) or (key >= 65 and key <= 90) or (key >= 48 and key <= 57) or (len(name) > 0 and key == 32)):
            name += chr(key)
        elif(key == 8):
            if(len(name) > 0): name = name[:len(name)-1]

    return name

    
