"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="pytest-repo-structure")
def main() -> None:
    """Pytest Repo Structure."""


if __name__ == "__main__":
    app()  # pragma: no cover
