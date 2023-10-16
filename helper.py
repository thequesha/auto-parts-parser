from termcolor import colored


def success(text=''):
    print(colored(text, 'green'))


def warning(text=''):
    print(colored(text, 'yellow'))


def danger(text=''):
    print(colored(text, 'red'))
