from timeit import default_timer as timer
import torch



device = torch.device("cuda")           
print(device)
n = 10_000_000
a = torch.ones(n, dtype = torch.float64, device=device)
torch.cuda.synchronize()

start = timer()
a += 1
torch.cuda.synchronize()
end = timer()
print("GPU Time:", end-start)
    
