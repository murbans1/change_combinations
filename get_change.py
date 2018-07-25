import click
import json

from change import calculate_changes
from clean_input import clean_input
from output_formatter import format_output


@click.command()
@click.argument('amount')
def get_change(amount):
    cleaned_input = clean_input(amount)
    if not cleaned_input:
        output = format_output('', [], error='wrong input!')
        click.echo(output)
        return

    value = float(cleaned_input)
    changes = calculate_changes(value)
    output = format_output(value, changes)
    click.echo('%s' % json.dumps(output))


if __name__ == '__main__':
    get_change()
