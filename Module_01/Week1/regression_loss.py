import math
import random


def calc_ae(y, y_hat):
    return abs(y - y_hat)


def calc_se(y, y_hat):
    return (y - y_hat)**2


def regression_loss():
    num_samples = input(
        'Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    loss_name = input('Input loss name: ')
    num_samples = int(num_samples)
    final_loss = 0

    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)
        if loss_name == 'MAE':
            loss = calc_ae(target, pred)
        else:
            loss = calc_se(target, pred)
        print(
            f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')
        final_loss += loss

    final_loss /= num_samples
    if loss_name == 'RMSE':
        final_loss = math.sqrt(final_loss)
    print(f'final {loss_name}: {final_loss}')


if __name__ == "__main__":
    regression_loss()
