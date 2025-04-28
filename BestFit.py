def best_fit_memory_allocation(block_sizes, process_sizes):
    n = len(block_sizes)
    m = len(process_sizes)

    allocation = [-1] * m  # To store which block is allocated to which process

    for i in range(m):  # For each process
        best_idx = -1
        for j in range(n):  # Search for best-fit block
            if block_sizes[j] >= process_sizes[i]:
                if best_idx == -1 or block_sizes[j] < block_sizes[best_idx]:
                    best_idx = j
        
        # Allocate the found block
        if best_idx != -1:
            allocation[i] = best_idx
            block_sizes[best_idx] -= process_sizes[i]

    # Print the results
    print("\nProcess No.\tProcess Size\tBlock No.")
    print("-------------------------------------------")
    for i in range(m):
        print(f"{i+1}\t\t{process_sizes[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

# Example usage
if __name__ == "__main__":
    block_sizes = [100, 500, 200, 300, 600]
    process_sizes = [212, 417, 112, 426]

    print("Best Fit Memory Allocation Algorithm")
    best_fit_memory_allocation(block_sizes.copy(), process_sizes)
