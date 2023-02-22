#!/usr/bin/env python
# imports
from __future__ import division
import os
import sys
import vcf
import time
import logging
from pathlib import Path
from typing import List, Optional
import typer
from vcf.parser import _Info as VcfInfo, _Format as VcfFormat, _vcf_metadata_parser as VcfMetadataParser
from .concat_helpers import concat_mafs

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)

logger = logging.getLogger("filter")

app = typer.Typer(help="merge multiple maf files produced by variants callers as part of the postprocessing process.")


def check_maf(files: List[Path]):
    # check that we have a list of mafs after reading off the cli
    extensions = [os.path.splitext(f)[1] for f in files]
    for ext in extensions:
        if ext != '.maf':
            typer.secho(f"If using files argument, all files must be mafs.", fg=typer.colors.RED)
            raise typer.Abort()
    return files 

def check_txt(paths: Path):
    # check that we have a text file after reading off the cli
    extension = os.path.splitext(paths)[1]
    if extension != '.txt':
        typer.secho(f"If using paths argument, must provided an input txt file.", fg=typer.colors.RED)
        raise typer.Abort()
    return paths

@app.command("maf")
def maf_maf(
    #TODO change args to be relevant to concat
    # I think this should be a list of mafs?
    files: List[Path] = typer.Option(
        None, 
        "--files",
        "-f",
        help="MAF file to concatenate. Maf files are specified here, or using paths parameter.",
        callback = check_maf
    ),
    paths: Path = typer.Option(
        None,
        "--paths",
        "-p",
        help="A text file containing paths of maf files to concatenate. Maf files are specified here, or using files parameter.",
        callback = check_txt
    ),
    output_maf: str = typer.Option(
        "output_maf",
        "--output",
        "-o",
        help="Maf output file name."
    )
):
    logger.info("started concat")
    # make sure files or paths was specified
    # as of < 0.7.0 does not support mutually exclusive arguments
    if not (files or paths): 
        typer.secho(
            f"Either paths, or files must be specified for concatenation to run.",
            fg=typer.colors.RED)
        raise typer.Abort()
    # process our paths txt file 
    if paths:
        opaths = open(paths, 'r')
        files = []
        for line in opaths.readlines():
            files.append(line.rstrip('\n').split(',')[0])
    # concat maf files 
    # paths vs files is taken care of at this point
    concat_mafs(files, output_maf)
    return 0


if __name__ == "__main__":
    app()
