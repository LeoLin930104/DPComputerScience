import context as c

def menu1(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = "I'm the main menu"
    options = [
        c.create_menu_item(1, "I am option 1", menu1_a),
        c.create_menu_item(2, "I am option 2", menu1_b),
        c.create_menu_item(3, "I am option 3", menu1_c),
        c.create_menu_item(4, "I am option 4", menu1_d)
    ]
    menu[c.OPTIONS] = options
    c.draw_menu(ctx, menu)

def menu1_a(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = "You chose option 1... The Game Literally Ends... Press Enter or ESC to exit the game"
    options = [
        c.create_menu_item(1, "I am option 1 in option 1", None),
        c.create_menu_item(2, "I am option 2 in option 1", None),
        c.create_menu_item(3, "I am option 3 in option 1", None),
        c.create_menu_item(4, "I am option 4 in option 1", None)
    ]
    menu[c.OPTIONS] = options
    c.draw_menu(ctx, menu)

def menu1_b(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = "You chose option 2... The Game Literally Ends... Press Enter or ESC to exit the game"
    options = [
        c.create_menu_item(1, "I am option 1 in option 2", None),
        c.create_menu_item(2, "I am option 2 in option 2", None),
        c.create_menu_item(3, "I am option 3 in option 2", None),
        c.create_menu_item(4, "I am option 4 in option 2", None)
    ]
    menu[c.OPTIONS] = options
    c.draw_menu(ctx, menu)

def menu1_c(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = "You chose option 3... The Game Literally Ends... Press Enter or ESC to exit the game"
    options = [
        c.create_menu_item(1, "I am option 1 in option 3", None),
        c.create_menu_item(2, "I am option 2 in option 3", None),
        c.create_menu_item(3, "I am option 3 in option 3", None),
        c.create_menu_item(4, "I am option 4 in option 3", None)
    ]
    menu[c.OPTIONS] = options
    c.draw_menu(ctx, menu)

def menu1_d(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = "You chose option 4... The Game Literally Ends... Press Enter or ESC to exit the game"
    options = [
        c.create_menu_item(1, "I am option 1 in option 4", None),
        c.create_menu_item(2, "I am option 2 in option 4", None),
        c.create_menu_item(3, "I am option 3 in option 4", None),
        c.create_menu_item(4, "I am option 4 in option 4", None)
    ]
    menu[c.OPTIONS] = options
    c.draw_menu(ctx, menu)
if __name__ == "__main__":
    context = c.init()
    menu1(context)
