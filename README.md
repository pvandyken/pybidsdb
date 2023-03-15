# PybidsDB

[Pybids](https://github.com/bids-standard/pybids) databases let you read `BIDSLayouts` in the blink of an eye, and are practically mandatory when iteratively developing workflows using tools like [snakebids](https://github.com/akhanf/snakebids). This library implements a command-line solution to generating these layouts.

By default, the database is generated on `/tmp`, which is assumed to mounted to a local or in-memory filesystem. This is important for datasets stored on NAS, as writing SQL to these systems takes a very, very, very long time. The library also enforces a special integration with AllianceCan's compute network: if SLURM commands like `sbatch` or `srun` are available, the app checks if the `$SLURM_TMPDIR` variable is defined to make sure a compute node is being used. If the variable is found, it will be used to generate the database.

In any case, after generation, the database is moved to the `.pybids` directory in the top level of your dataset, or in another directory of your choosing.

```
Usage: pybidsdb [options] [path]

Arguments:
    path: Path of the dataset (defaults to current directory)
    
    --force: Force run on the login node (by default only runs on compute nodes)
    --validate: Run bids validation on the dataset
    --derivatives: Include derivatives found in the `dataset/derivatives` folder
    --folder: Name of the database folder (e.g. `dataset/<folder>`)
```

## Installation

Install with [pipx](https://pypi.org/project/pipx/):

```
pipx install git+https://github.com/pvandyken/pybidsdb.git
```
