import os
from collections import defaultdict

def count_file_types(directory):
    file_types_count = defaultdict(int)
    
    # Walk through each file in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Get the file extension
            _, ext = os.path.splitext(file)
            # Increment the count for this file type
            file_types_count[ext.lower()] += 1
    
    return file_types_count

# Specify the directory path
directory_path = '/path/to/directory'

# Count file types and print results
file_counts = count_file_types(directory_path)
for ext, count in file_counts.items():
    print(f"{ext if ext else 'No Extension'}: {count} files")
