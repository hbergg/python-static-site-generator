import typer
from ssg.site import Site

def main(source = "content",dest = "dist"):
    config = {'source': source, 'dest': dest}
    #print(config)
    s = Site(**config)

if __name__ == "__main__":
    typer.run(main)