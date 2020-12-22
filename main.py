#!/usr/bin/env python
import click
CONTEXT_SETTINGS = {'help_option_names':['-h', '--help', '-?']}

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('rows', type=click.IntRange(1))
@click.argument('columns', type=click.IntRange(1))
@click.option('--headers', help="space-seperated string of column headers. MUST be of length columns")
@click.option('--inputs', help="space-seperated string of cell values. MUST be of length columns * rows")
def create_table(rows, columns, headers, inputs):
    headers = headers.split(' ') if headers else [f"header{x}" for x in range(columns)]
    inputs = inputs.split(' ') if inputs else generate_placeholder_inputs(columns, rows)
    res = create_row(columns, headers)
    res += create_row(columns, ["---" for i in range(columns)])
    for i in range(rows):
        cell_values=inputs[i*columns:i*columns+columns]
        res += create_row(columns, cell_values)
    click.echo(f"{res}")
    return res;

def create_row(columns, inputs):
    if columns != len(inputs):
        raise ValueError(f"Invalid input length. Excpected: {columns} Actual:{len(inputs)}")
    res="|"
    for i in range(columns):
        res += f"{inputs[i]}|"
    res+="\n"
    return res;

def generate_placeholder_inputs(columns, rows):
    res = []
    for i in range(rows):
        row_label = chr(ord('a')+i)
        res += [f"{row_label}{i}" for i in range(columns)]
    return res
