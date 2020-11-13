import curses

MENU = "menu"
OPTIONS = "options"
PROMPT = "prompt"
SCREEN = "screen"
POS = "position"
TEXT = "text"
CALLBACK = "callback"
STATUS_FORMAT = "Option: {:>2} |Key: {:>5} | Active: {:>2}"

def create_menu_item(pos:int, text: str, callback: callable) -> dict:
    menu_item = { POS: pos, TEXT: text, CALLBACK: callback }
    return menu_item

def handle_click(ctx: list, menu: dict, active: int) -> None:
    options = menu[OPTIONS]
    if ( options[active]and options[active][CALLBACK] ): return options[active][CALLBACK](ctx)

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

    # Event loop. Listens for key presses from the user
    while(key != 27):

        # Later insert key actions
        if  ( key == 456 or key == 115 ): active = (active + 1) % len(options)
        elif( key == 450 or key == 119 ): active = (active - 1) % len(options) 
        elif( key == 10 ): return handle_click(ctx, menu, active)
            
        # Clear Screen
        scr.clear()
        h, w = scr.getmaxyx()

        # Add text prompt
        scr.addstr(2, 3, prompt)
        
        # Draw Menu Here
        for idx, option in enumerate(options):
            if(idx == active):
                scr.attron(curses.color_pair(3))
                scr.addstr(4 + idx, 8, option[TEXT])
                scr.attroff(curses.color_pair(3))
            else: scr.addstr(4 + idx, 8, option[TEXT])

        # Draw Status Bar
        status_string = STATUS_FORMAT.format(active+1, key, active+1)
        scr.attron(curses.color_pair(4))
        scr.addstr(h-1, 0, status_string)
        scr.addstr(h-1, len(status_string), ' ' * (w - len(status_string) - 1))
        scr.attroff(curses.color_pair(4))
        scr.move(h-1,w-2)
        scr.refresh()

        # Get Next Key
        key = scr.getch()