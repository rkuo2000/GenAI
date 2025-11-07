import torch

# Check if CUDA is available
if not torch.cuda.is_available():
    print("CUDA is not available. No GPUs found.")
else:
    # Get the number of available GPUs
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs available: {num_gpus}")

    # Iterate through each GPU and print its details
    for i in range(num_gpus):
        print(f"\nGPU {i}:")
        print(f"  Name: {torch.cuda.get_device_name(i)}")
        print(f"  Capability: {torch.cuda.get_device_capability(i)}")
        #print(f"  Current device index: {torch.cuda.current_device()}") # Note: This will likely be the same for all if not explicitly set per process
        # You can get more specific memory details if needed
        total_memory = torch.cuda.get_device_properties(i).total_memory / (1024**3)
        print(f"  Total Memory: {total_memory:.2f} GB")
