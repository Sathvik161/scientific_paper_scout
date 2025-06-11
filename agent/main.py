import typer
from agent_host import run_agent

app = typer.Typer()

@app.command()
def chat():
    typer.echo("Welcome to Scientific Paper Scout!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = run_agent(user_input)
        print(response)

if __name__ == "__main__":
    app()
