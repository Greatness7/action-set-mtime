# action-set-mtime
A github action for setting the modification times of specified files.

Git unfortunately does not preserve file metadata like modification time. This is problematic if you're stuck with a system where such metadata is important. 

This action allows you to automate the process of correcting file modification times. Typically this would be done as part of a larger release process, prior to collecting said files into a compressed archive.

## Basic Usage

```yaml
on:
  push:
    tags:
      - "v*"
jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repo
        uses: actions/checkout@v2

      - name: set modification times
        uses: greatness7/action-set-mtime@v1
        with:
          times: |
            "**/OAAB_Data.esm" = 1577854800
            "**/OAAB_Cells.esp" = 1577854800
```

## Paramaters

- **times**

    *A string containing glob patterns and the modification times to be applied to files matching said patterns.*

    *Patterns and their associated times must be delimited by an `=` character.*
    
    *Only one pattern/time entry is allowed per line. Use separate lines to specify additional entries.*
