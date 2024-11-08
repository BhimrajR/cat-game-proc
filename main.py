import os
import questionary
import pyfiglet
from rich.console import Console
from rich.color import Color
from rich.text import Text
from rich.progress import BarColumn, Progress, TextColumn

def ClearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ValidateString(userInput):
    if not userInput.isalpha():
        return "Input must contain only letters."
    return True

console = Console()

colourNames = [
    "red", "green", "blue", "yellow", "cyan", "magenta", "white", "black",
    "bright_red", "bright_green", "bright_blue", "bright_yellow", 
    "bright_cyan", "bright_magenta", "bright_white"
]
colourDict = {colourName.replace("_", " ").capitalize():colourName for colourName in colourNames}

cat_attributes = {
    "intelligence": 10,
    "energy": 100,
    "weight": 10,
    "hunger": 100,
    "happiness": 50,
    "hygiene": 50
}

ClearConsole()

print("Welcome to my cat game!")

name = questionary.text("Let's give your cat a name:", validate=ValidateString).ask().capitalize()
colour = questionary.select(
    "What colour do you want your cat to be?",
    choices=list(colourDict.keys())
).ask()

catColour = colourDict[colour]

while True:
    ClearConsole()

    if cat_attributes['energy'] <= 0:
        console.print(f"{name} has no energy left!", style="bold red")

    if cat_attributes['hunger'] <= 0:
        console.print(f"{name} is starving!", style="bold red")
        console.print(Text("-2 weight"), style="bold red")
        cat_attributes["weight"] -= 2

    if cat_attributes['hunger'] > 100:
        console.print(f"{name} is too full!", style="bold red")
        console.print(Text("+2 weight"), style="bold green")
        cat_attributes["weight"] += 2

    if cat_attributes['intelligence'] <= 0:
        console.print(f"{name} is feeling a bit clueless!", style="bold red")

    if cat_attributes['weight'] <= 0:
        console.print(f"{name} is too weak!", style="bold red")

    if cat_attributes['happiness'] <= 0:
        console.print(f"{name} is feeling very sad!", style="bold red")

    if cat_attributes['hygiene'] <= 0:
        console.print(f"{name} is too dirty!", style="bold red")

    proceed = questionary.select(
        "What would you like to do?",
        choices=["Play with your cat", "Train with your cat", "Feed your cat", "Rest your cat", "Wash your cat",  "Show stats", "Exit"],
    ).ask()

    match proceed:
        case "Play with your cat":
            if cat_attributes["energy"] < 15:
                console.print(f"{name} is too tired!", style="bold red")
                input("Press enter to continue.")
                continue
            elif cat_attributes["hunger"] < 10:
                console.print(f"{name} is too hungry!", style="bold red")
                input("Press enter to continue.")
                continue
            elif cat_attributes["hygiene"] < 10:
                console.print(f"{name} is too dirty!", style="bold red")
                input("Press enter to continue.")
                continue
            console.print(Text(pyfiglet.figlet_format("Play time"), style="bold black"))
            console.print(f"{name} is playing.", style="bold black")
            console.print(Text("""                                                  
           __..--''``\--....___   _..,_
       _.-'    .-/";  `        ``<._  ``-+'~=.
   _.-' _..--.'_    \                    `(^) )
  ((..-'    (< _     ;_..__               ; `'   
             `-._,_)'      ``--...____..-'
"""), style=catColour)
            console.print(Text("+15 happiness"), style="bold green")
            console.print(Text("-10 hunger"), style="bold red")
            console.print(Text("-15 energy"), style="bold red")
            console.print(Text("-10 hygiene"), style="bold red")
            cat_attributes["happiness"] += 15
            cat_attributes["hunger"] -= 10
            cat_attributes["energy"] -= 15
            cat_attributes["hygiene"] -= 10
            input("Press enter to continue.")
        case "Train with your cat":
            if cat_attributes["energy"] < 15:
                console.print(f"{name} is too tired!", style="bold red")
                input("Press enter to continue.")
                continue
            elif cat_attributes["hunger"] < 10:
                console.print(f"{name} is too hungry!", style="bold red")
                input("Press enter to continue.")
                continue
            elif cat_attributes["hygiene"] < 5:
                console.print(f"{name} is too dirty!", style="bold red")
                input("Press enter to continue.")
                continue
            console.print(Text(pyfiglet.figlet_format("Training"), style="bold black"))
            console.print(f"{name} is training.", style="bold black")
            console.print(Text("""                                                  
     _._     _,-'""`-._
     (,-.`._,'(       |\`-/| 
         `-.-' \ )-`( , o o)
               `-    \`_`"'- 
"""), style=catColour)
            console.print(Text("+10 happiness"), style="bold green")
            console.print(Text("+10 intelligence"), style="bold green")
            console.print(Text("-10 hunger"), style="bold red")
            console.print(Text("-15 energy"), style="bold red")
            console.print(Text("-5 hygiene"), style="bold red")
            cat_attributes["happiness"] += 10
            cat_attributes["intelligence"] += 10
            cat_attributes["hunger"] -= 10
            cat_attributes["energy"] -= 15
            cat_attributes["hygiene"] -= 5
            input("Press enter to continue.")
        case "Feed your cat":
            if cat_attributes["hunger"] > 100:
                console.print(f"{name} is too full!", style="bold red")
                input("Press enter to continue.")
                continue
            console.print(Text(pyfiglet.figlet_format("Eating"), style="bold black"))
            console.print(f"{name} is eating.", style="bold black")
            console.print(Text("""                                                  
      ,/|         _.--''^``-...___.._.,;
     /, \.     _-'          ,--,,,--'''
    { \    `_-''       '    /}
     `;;'            ;   ; ;
 ._.--''     ._,,, _..'  .;.' 
  (,_....----'''     (,..--'' 
"""), style=catColour)
            console.print(Text("+15 hunger"), style="bold green")
            cat_attributes["hunger"] += 15
            input("Press enter to continue.")
        case "Rest your cat":
            console.print(Text(pyfiglet.figlet_format("Resting"), style="bold black"))
            console.print(f"{name} is resting.", style="bold black")
            console.print(Text("""                                                  
     A.,.A
     (u u )\-=-__---===-.    
     `.^,,'  ,     (    \`-.   
   /~/~~~~~ /...;/~~~~~  (`\`. 
   ```~~~~~~~~~~~```~~~~~~,','
                          ` 
"""), style=catColour)
            console.print(Text("+20 energy"), style="bold green")
            console.print(Text("-5 hunger"), style="bold red")
            console.print(Text("-5 hygiene"), style="bold red")
            cat_attributes["energy"] += 20
            cat_attributes["hunger"] -= 5
            cat_attributes["hygiene"] -= 5
            input("Press enter to continue.")
        case "Wash your cat":
            console.print(Text(pyfiglet.figlet_format("Wash up"), style="bold black"))
            console.print(f"{name} is bathing.", style="bold black")
            console.print(Text("""                                                  
                  ,
                 \)\_
                /    '. .---._
              =P ^     `      '.
               `--.       /     |
               .-'(       \      |
              (.-'   )-..__>   , ;
              (_.--``    (__.-/ / 
                      .-.__.-'.'
                       '-...-'                        
"""), style=catColour)
            console.print(Text("+10 energy"), style="bold green")
            console.print(Text("+20 hygiene"), style="bold green")
            console.print(Text("-10 happiness"), style="bold red")
            cat_attributes["energy"] += 10
            cat_attributes["hygiene"] += 20
            cat_attributes["happiness"] -= 10
            input("Press enter to continue.")
        case "Show stats":
            console.print(Text(pyfiglet.figlet_format("Stats"), style="bold black"))
            console.print(f"Here are {name}'s stats:", style="bold black")
            console.print(Text("""                                                  
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
      .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
"""), style=catColour)

            with Progress(
                TextColumn("[bold blue]{task.description}", justify="right"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=console,
            ) as progress:
                for attribute, value in cat_attributes.items():
                    progress.add_task(description=attribute.capitalize(), total=100, completed=value)

            input("Press enter to continue.")
        case "Exit":
            console.print(f"Goodbye, {name} the {colour} cat!")
            break