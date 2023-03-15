import os
import shutil
import subprocess as sp
import sys
import tempfile as tmp
from pathlib import Path

import typer
from bids import BIDSLayout
from rich.console import Console

err = Console(stderr=True)
app = typer.Typer()


@app.command()
def main(
    path: Path = typer.Argument(".", help="Path of dataset"),
    force: bool = typer.Option(False, help="Force run on login node"),
    validate: bool = typer.Option(False, help="Force validation of dataset"),
    derivatives: bool = typer.Option(
        False, help="Index derivative datasets in `dataset/derivatives` folder"
    ),
    folder: str = typer.Option(".pybids", help="Name of database folder"),
):
    try:
        sp.check_call(["which", "srun", "||", "which", "sbatch"])
        slurm_avail = True
    except sp.CalledProcessError:
        slurm_avail = False

    if "SLURM_TMPDIR" in os.environ:
        tmpdir = Path(os.environ["SLURM_TMPDIR"]) / ".pybids"
        tmpdir.mkdir()
    else:
        if slurm_avail and not force:
            err.print(
                "This command should be run on a compute node (use --force to run "
                "anyway)",
                style="red1",
            )
            exit(1)
        tmpdir = Path(tmp.mkdtemp(prefix="pybidsdb_"))

    if not path.exists():
        err.print(f"Path {path} does not exist", style="red1")
        exit(1)

    stagedir = path / f"{folder}.tmp"
    final = path / folder

    if stagedir.exists():
        err.print(
            f"Found exisiting directory {stagedir}. A previous run may have been "
            "interrupted.",
            style="red1",
        )
        exit(1)
    print(f"Writing database to {tmpdir}")
    BIDSLayout(path, derivatives=derivatives, database_path=tmpdir, validate=validate)

    print(f"Moving to {final}")
    shutil.move(str(tmpdir), stagedir)
    if final.exists():
        print("Removing old database")
        shutil.rmtree(final)
    shutil.move(stagedir, final)


if __name__ == "__main__":
    typer.run(main)
