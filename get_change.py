import click
import json

from change import calculate_changes
from clean_input import clean_input


@click.command()
@click.argument('amount')
def get_change(amount):
    cleaned_input = clean_input(amount)
    if not cleaned_input:
        click.echo('wrong input!')

    value = float(cleaned_input)
    changes = calculate_changes(value)
    click.echo('%s' % json.dumps(changes))


if __name__ == '__main__':
    get_change()
