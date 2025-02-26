from pathlib import Path
from rich.markup import escape
from rich import print
from typing_extensions import Annotated
import typer

def main (
        hidden: Annotated[bool, typer.Option(help="Include hidden files")] = False,
):
    path = Path('.')
    print(f"hidden is {hidden}")
    # HIDDEN FILES
    if hidden:
        for x in path.iterdir():
            if x.is_dir():
                print(f"[bold blue]{escape(str(x))}[/bold blue]")
            else:
                print(str(x))

    # STANDARD PRINTING
    for x in path.iterdir():
        if x.is_dir() and not x.name.startswith('.'):
            print(f"[bold blue]{escape(str(x))}[/bold blue]")
        elif not x.name.startswith('.'):
            print(str(x))



if __name__ == '__main__':
    typer.run(main)

