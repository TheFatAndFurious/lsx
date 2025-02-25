from pathlib import Path
from rich.markup import escape
from rich import print

def main ():
    path = Path('.')
    for x in path.iterdir():
        if x.is_dir():
            print(f"[bold]{escape(str(x))}[/bold]")
        else:
            print(str(x))

if __name__ == '__main__':
    main()

