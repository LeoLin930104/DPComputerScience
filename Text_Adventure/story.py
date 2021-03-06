import context as c
import sys

title = "Mysterious Forest"
recursion_limit = 100
story = "Leo Lin"
program = "Leo Lin"
gameover_format = """Sad, Solemn, and Sorry. Still, you need to watch the Credit:
    {}: {},
    {}: {},
    Yes, It is short, and I am the only one who wrote this thing, Now:"""
congradulations_format = """You are the Champion. You are the One. You are watching the Credit:
    {}: {},
    {}: {},
    Yes, It is short, and I am the only one who wrote this thing, Now:"""


def main(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """Traveller, you woke up in the \"Mysterious Forest\". Since you have been travelling, you are quite hungry and thursty
    You see fruits that you have never seen before growing on a tree. 
    You see a pond, it contains water-like liquid that is luminating.
    You see a sign in front of a clear path that says \"LEAVE BEFORE DAWN!\"
    What will you do?"""
    options = [
        c.create_menu_item(1, 'Eat the "Mysterious Fruit"...', main_fruit),
        c.create_menu_item(2, 'Drink the "Luminous Water"...', main_water),
        c.create_menu_item(3, 'Follow the "Sign"...', main_sign),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """The \"Mysterious Fruit\" is horrible and not endurable.
    You spit it out with a signiture of disgust.
    But considing your hunger, recovery is still important.
    What will you do?"""
    options = [
        c.create_menu_item(
            1, 'Bear the taste and continue to "Eat"...', main_fruit_eat
        ),
        c.create_menu_item(
            2, 'Try, as complement, the "Luminous Water"...', main_fruit_water
        ),
        c.create_menu_item(3, 'Without the fruit, go down the "Path"', main_fruit_path),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit_eat(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """You have finished all the fruits on the tree.
    Besides of the disgustingness, you have over come your hunger and thurst from the fruit.
    The time now seems to be passing noon.
    What will you do?"""
    options = [
        c.create_menu_item(
            1,
            'With all the curiosity, try the "Luminous Water"...',
            main_fruit_eat_water,
        ),
        c.create_menu_item(3, 'Go down the "Path"...', main_fruit_eat_path),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit_eat_water(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """After taking a small sip of the luminous liquid,
    your throat felt like burning, your tongue felt like melting.
    Your life is now depending on this brisk.
    What will you do?"""
    options = [
        c.create_menu_item(
            1, 'Eat the "Mysterious Fruit"...', main_fruit_eat_water_eat
        ),
        c.create_menu_item(
            2, 'Run down the path and search for "Help"...', main_fruit_eat_water_path
        ),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit_eat_water_eat(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """Maybe, it was the cure. Maybe, it could save me.
    There is nothing left on the tree. There is nothing else I can do
    With the left of a few thoughts, you mind fades into the \"Rising Heat\"..."""
    options = [c.create_menu_item(1, "Game Over...", restart_gameover)]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit_eat_water_path(ctx: dict) -> None:
    menu[
        c.PROMPT
    ] = """In your sight, the path becomes longer, longer, and longer...
    In you mind, the time becomes slower, slower, and slower...
    Without a sight of anyone, you comes to an \"Eternal Sleep\"..."""
    options = [c.create_menu_item(1, "Game Over...", restart_gameover)]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit_eat_path(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """By the help of the fruit, you have a overwhelming stamina.
    Without any exhaution, you are, yes,
    back to the \"Path\" you are familiar with."""
    options = [c.create_menu_item(1, "Congradulations.", restart_congradulations)]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_fruit_water(ctx: dict) -> None:
    return main_water(ctx)


def main_fruit_path(ctx: dict) -> None:
    return main_sign(ctx)


def main_water(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """After taking a small sip of the luminous liquid,
    your throat felt like burning, your tongue felt like melting.
    Your life is now depending on this brisk.
    What will you do?"""
    options = [
        c.create_menu_item(1, 'Eat the "Mysterious Fruit"...', main_water_fruit),
        c.create_menu_item(
            2, 'Run down the path and search for "Help"...', main_water_help
        ),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_water_fruit(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """With all the luck, this fruit have healed your tongue, recovered your throat
    Without all the luck, this fruit is disgustingly bad to eat.
    Without all the luck, you have taken time to recover your lost stamina from the poison.
    The time is closing to Dawn.
    What will you do?"""
    options = [
        c.create_menu_item(1, 'Run down the "Path"...', main_water_fruit_path),
        c.create_menu_item(
            2,
            'Collect the mysterious fruit and prepare for the arrival of the "Night"...',
            main_water_fruit_night,
        ),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_water_fruit_path(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """Surprisingly, the fruit have gave you stamina better than you thought
    You have exhausted youself, but you have reached the end of the path,
    back, to the \"Path\" you are familiar with."""
    options = [
        c.create_menu_item(1, "Congradulations.", restart_congradulations),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_water_fruit_night(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """You thought you are ready. You thought you are prepared.
    But the Mysterious Forest will chase you down.
    Until, you are part of the Mysterious Forest."""
    options = [
        c.create_menu_item(1, "Game Over...", restart_gameover),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_water_help(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """In your sight, the path becomes longer, longer, and longer...
    In you mind, the time becomes slower, slower, and slower...
    Without a sight of anyone, you comes to an \"Eternal Sleep\"..."""
    options = [c.create_menu_item(1, "Game Over...", restart_gameover)]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_sign(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """This path is Much, Much, Much longer than expected.
    You feel so powerless from the sense of hunger and thurst,
    but going back to seek for the \"Mysterious Fruit\" may take too long.
    What will you do?"""
    options = [
        c.create_menu_item(1, 'Continue on the "Path"...', main_sign_path),
        c.create_menu_item(2, 'Retrieve the "Mysterious Fruit"...', main_sign_fruit),
        c.create_menu_item(
            3, 'Try to search for food from "Surroundings"...', main_sign_search
        ),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_sign_path(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """Yes, too long, this path is.
    For another step you gain, another part of you to lose.
    The Exhaustion, the pain, is never going away from upcoming \"Eternal Sleep\"..."""
    options = [c.create_menu_item(1, "Game Over...", restart_gameover)]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_sign_fruit(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """You have returned to the orignal place.
    You have eaten some \"Mysterious Fruit\" to restore you stamina.
    The time is closing Dawn.
    What will you do?"""
    options = [
        c.create_menu_item(1, 'Run down the "Path"...', main_sign_fruit_path),
        c.create_menu_item(
            2,
            'Collect the mysterious fruit and prepare for the arrival of the "Night"...',
            main_sign_fruit_night,
        ),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_sign_fruit_path(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """Surprisingly, the fruit have gave you stamina better than you thought
    You have exhausted youself, but you have reached the end of the path,
    back, to the \"Path\" you are familiar to."""
    options = [
        c.create_menu_item(1, "Game Over...", restart_gameover),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_sign_fruit_night(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """You thought you are ready. You thought you are prepared.
    But the Mysterious Forest will chase you down.
    Until, you are part of the Mysterious Forest."""
    options = [
        c.create_menu_item(1, "Game Over...", restart_gameover),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def main_sign_search(ctx: dict) -> None:
    menu = {}
    menu[
        c.PROMPT
    ] = """With all the luck, you have managed to find another mysterious tree that has mysterious fruit.
    You have used the mysterious fruit for restoring.
    By the time you have reached the end of the path,
    you are, yes, back to the \"Path\" you are familiar with."""
    options = [
        c.create_menu_item(1, "Congradulations.", restart_congradulations),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def restart_gameover(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = gameover_format.format(
        c.STORY, c.CREDIT[c.STORY], c.PROGRAM, c.CREDIT[c.PROGRAM]
    )
    options = [
        c.create_menu_item(1, "Restart...", main),
        c.create_menu_item(2, "Exit...", c.terminate),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def restart_congradulations(ctx: dict) -> None:
    menu = {}
    menu[c.PROMPT] = congradulations_format.format(
        c.STORY, c.CREDIT[c.STORY], c.PROGRAM, c.CREDIT[c.PROGRAM]
    )
    options = [
        c.create_menu_item(1, "Restart...", main),
        c.create_menu_item(2, "Exit...", c.terminate),
    ]
    menu[c.OPTIONS] = options
    return c.draw_menu(ctx, menu)


def constructor(title: str, recursion_limit: int, story: str, program: str) -> None:
    c.TITLE = title
    c.RECURSION_LIMIT = recursion_limit
    sys.setrecursionlimit(recursion_limit)
    c.CREDIT[c.STORY] = story
    c.CREDIT[c.PROGRAM] = program


def init():
    context = c.init()
    try:
        constructor(title, recursion_limit, story, program)
        c.NAME = c.enter_name(context)
        callback = main(context)
        while callback != None:
            callback = callback(context)
    except RecursionError as e:
        c.play_too_long(context)


if __name__ == "__main__":
    init()
