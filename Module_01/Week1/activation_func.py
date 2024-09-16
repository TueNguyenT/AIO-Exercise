import math


def calc_sig(x):
    return 1 / (1 + math.exp(-x))


def calc_relu(x):
    return 0 * (x <= 0) + x * (x > 0)


def calc_elu(x, alpha=0.01):
    return alpha * (math.exp(x) - 1) * (x <= 0) + x * (x > 0)


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def calc_activation_func():
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return

    act_name = input('Input activation Function (sigmoid|relu|elu): ')
    if act_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{act_name} is not supproted')
        return

    x = float(x)
    if act_name == 'sigmoid':
        res = calc_sig(x)
    elif act_name == 'relu':
        res = calc_relu(x)
    else:
        res = calc_elu(x)
    print(f'{act_name}: f({x}) = {res}')


if __name__ == "__main__":
    calc_activation_func()
