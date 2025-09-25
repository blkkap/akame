from timeit import default_timer as timer
import torch

def func(a):
    for i in range(10000000):
        a[i] += 1


if __name__=="__main__":
    device = torch.device("cuda")
    print(device)
    n = 10000000
    a = torch.ones(n, dtype = torch.float64, device=device)

    start = timer()
    func(a)
    print("GPU Time:", timer()-start)
    
