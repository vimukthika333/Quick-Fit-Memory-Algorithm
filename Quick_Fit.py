class QuickFitAllocator:  
    def __init__(self, sizes):  
        """  
        Initialize the Quick Fit memory allocator.  
        
        :param sizes: List of fixed sizes for memory pools.  
        """  
        self.sizes = sizes                    # sizes of the fixed memory pools  
        self.memory_pools = {size: [] for size in sizes}  # dictionary to hold free lists for each size  
        self.used_memory = {size: [] for size in sizes}   # dictionary to track allocated memory of each size  
        self.total_memory = {size: 0 for size in sizes}    # total memory for each pool for simulation purpose  

    def allocate(self, size):  
        """  
        Allocates a block of memory of the given size using the Quick Fit algorithm.  
        
        :param size: Size of the memory block to allocate.  
        :return: Identifier of the allocated block or None if allocation failed.  
        """  
        if size not in self.memory_pools:  
            print(f"Error: Size {size} is not supported.")  
            return None  
        
        if self.memory_pools[size]:  
            # If there is a free block available, allocate it  
            block = self.memory_pools[size].pop()  
            self.used_memory[size].append(block)  # Mark it as used  
            print(f"Allocated block of size {size}: {block}")  
            return block  
        else:  
            # If no free blocks, create a new one  
            block_id = self.total_memory[size]  
            self.total_memory[size] += 1  
            self.used_memory[size].append(block_id)  # Mark the new block as used  
            print(f"Allocated new block of size {size}: {block_id}")  
            return block_id  

    def deallocate(self, size, block_id):  
        """  
        Deallocates a block of memory of the given size and identifier.  
        
        :param size: Size of the memory block to deallocate.  
        :param block_id: Identifier of the block to deallocate.  
        :return: True if successfully deallocated, False otherwise.  
        """  
        if size not in self.used_memory or block_id not in self.used_memory[size]:  
            print(f"Error: Block {block_id} of size {size} not found.")  
            return False  
        
        self.used_memory[size].remove(block_id)  # Remove it from used memory  
        self.memory_pools[size].append(block_id)  # Add it back to the free list  
        print(f"Deallocated block of size {size}: {block_id}")  
        return True  

    def status(self):  
        """  
        Displays the current status of the memory pools and used memory.  
        """  
        print("Memory status:")  
        for size in self.sizes:  
            print(f"  Size {size} - Free: {len(self.memory_pools[size])}, Used: {len(self.used_memory[size])}")  

# Example Usage  
if __name__ == "__main__":  
    # Define fixed sizes for the memory pools  
    fixed_sizes = [16, 32, 64, 128]  
    
    # Create the Quick Fit Memory Allocator  
    allocator = QuickFitAllocator(fixed_sizes)  
    
    # Allocate some memory blocks  
    blocks_16_1 = allocator.allocate(16)  
    blocks_32_1 = allocator.allocate(32)  
    blocks_16_2 = allocator.allocate(16)  
    
    # Check status of memory pools  
    allocator.status()  
    
    # Deallocate a block  
    allocator.deallocate(16, blocks_16_1)  
    
    # Check status of memory pools again  
    allocator.status()  
    
    # Try allocating again after deallocation  
    blocks_16_3 = allocator.allocate(16)  
    
    # Final status  
    allocator.status()  
