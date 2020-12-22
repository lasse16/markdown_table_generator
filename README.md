# Markdown Table Generator

This is a quick markdown table generator with a proper cli-documentation.

## Installation
Install via pip by cloning the source and then including the module by `setuptools`.
```
pip install -U .
```
The module name is `table_generator`, which can also be found in `setup.py`.

## Usage
``` bash
generate_table <ROWS> <COLUMNS> [--headers="header0 header1 ... header<COLUMNS>"] [--inputs="a0 a1 ... a<COLUMNS> b0 b1 ... <ROWS as char><COLUMNS>"]

# example
generate_table 2 3
> | header0 | header1 | header2 |
> | ---     | ---     | ---     |
> | a0      | a1      | a2      |
> | b0      | b1      | b2      |

generate_table 2 3 --headers="x y z" --inputs="ax ay az ba by bz"
> | x   | y   | z   |
> | --- | --- | --- |
> | ax  | ay  | az  |
> | ba  | by  | bz  |
```

