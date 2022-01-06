import os

from pathlib import Path

if __name__ == "__main__":
    for line in os.environ['TIMES'].splitlines():
        try:
            pattern, mtime = line.split("=", maxsplit=1)
        except ValueError:
            raise ValueError(f"Line does not contain expected delimiter (=) : {line}")

        try:
            mtime = int(mtime)
        except:
            raise ValueError(f"Invalid timestamp (could not convert to int) : {mtime}")

        # strip quotes if the pattern was quoted
        if '"' in pattern:
            pattern = pattern.strip().strip('"')

        for file in Path.cwd().glob(pattern):
            if file.is_file():
                old_metadata = file.stat()
                os.utime(file, (old_metadata.st_atime, mtime))
                new_metadata = file.stat()
                print(f"Updated mtime for {file}")
                print(f"\t{old_metadata.st_mtime} -> {new_metadata.st_mtime}")
