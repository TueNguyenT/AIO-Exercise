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
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = MySoftmax()
    softmax_stable = SoftmaxStable()
    print(softmax(data))
    print(softmax_stable(data))
