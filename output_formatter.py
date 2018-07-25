

def format_output(amount, results, error=None):
    return {
        'input': '$%s' % amount,
        'output': results,
        'error': error
    }