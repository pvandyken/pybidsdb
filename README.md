# PybidsDB

[Pybids](https://github.com/bids-standard/pybids) databases let you read `BIDSLayouts` in the blink of an eye, but creating them on NAS (like the scratch dir on AllianceCan's Graham compute cluster) takes a very, very, very long time. The solution is to create the database on local scratch or in an in-memory tmpdir, then move it to the desired destination. This library facilitates this process.

```
Usage: pybidsdb [options] [path]

Arguments:
    path: Path of the dataset (defaults to current directory)
    
    --force: Force run on the login node (by default only runs on compute nodes)
    --validate: Run bids validation on the dataset
    --derivatives: Include derivatives found in the `dataset/derivatives` folder
    --folder: Name of the database folder (e.g. `dataset/<folder>`
```

## Installation

Install with [pipx](https://pypi.org/project/pipx/):

```
pipx install git+https://github.com/pvandyken/pybidsdb.git
```
