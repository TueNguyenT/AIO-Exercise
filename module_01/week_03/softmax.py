import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = torch.sum(x_exp)
        return x_exp / partition


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x)
        x_exp = torch.exp(x - x_max)
        partition = torch.sum(x_exp)
        return x_exp / partition


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = MySoftmax()
    output = softmax(data)
    print(output)

    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)
