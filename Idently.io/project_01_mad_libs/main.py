from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.theme import Theme
from rich.panel import Panel

NOUN_STYLE = Style(color="Cyan", bold=True)
ADJECTIVE_STYLE = Style(color="bright_red", bold=True)
VERB_STYLE = Style(color="#F78B00", bold=True)

theme_app = Theme({
    "noun": NOUN_STYLE,
    "adjective": ADJECTIVE_STYLE,
    "verb": VERB_STYLE
})

def get_input(word_type:str, type=str) -> str| None:
    
    while True:
        
        text = type(input(f"Enter a {word_type}: "))
        
        # rejeita vazio
        if not text:
            print("It can be an empty Value.")
            continue

        # rejeita boolean
        if text.lower() in ("true", "false"):
            print("Do not type a boolean (true/false).")
            continue

        # rejeita número
        try:
            float(text)
            print("Do not type a number.")
            continue
        except ValueError:
            pass  # não é número, o

        return text

def main() -> None:
    
    console = Console(theme=theme_app)
    
    noun_01 = get_input("noun")
    adjective_01 = get_input("adjective") 
    verb_01 = get_input("verb")
    noun_02 = get_input("noun")
    verb_02 = get_input("verb")

    story = f"""
    Once upon a time, there was a [adjective]{adjective_01}[/] [noun]{noun_01}[/] who loved to [verb]{verb_01}[/] all day.

    One day, [noun]{noun_02}[/] walked into the room and caught the [noun]{noun_01}[/] in the act. 

    [noun]{noun_02}[/]: "What are you doing?"
    [noun]{noun_01}[/]: "I'm just {verb_01}ing, what's the big deal?"
    [noun]{noun_02}[/]: "Well, it's not every day that you see a [noun]{noun_01}[/] [verb]{verb_01}ing[/] in the middle of the day."
    [noun]{noun_01}[/]: "I guess you're right. Maybe I should take a break."
    [noun]{noun_02}[/]: "That's probably a good idea. Why don't we go [verb]{verb_02}[/] instead?"
    [noun]{noun_01}[/]: "Sure, that sounds like fun!"

    And so, [noun]{noun_02}[/] and the [noun]{noun_01}[/] went off to [verb]{verb_02}[/] and had a great time. 
    
    The end.
    """

    painel = Panel(story, expand=False, title="Mad Libs")

    console.print(painel)
    

if __name__ == "__main__":
    main()
    