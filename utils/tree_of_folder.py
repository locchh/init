import os
import sys

def generate_tree(path, prefix=""):
    # Get the list of items in the current directory
    items = os.listdir(path)
    
    # Count the number of items to handle the last item differently
    total_items = len(items)
    
    for index, item in enumerate(items):
        # Create the full path to the item
        item_path = os.path.join(path, item)
        
        # Determine if this is the last item in the current directory
        is_last = index == total_items - 1
        
        # Print the item
        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)
        
        # If the item is a directory, recurse into it
        if os.path.isdir(item_path):
            # Create a new prefix for the next level of indentation
            new_prefix = prefix + ("    " if is_last else "│   ")
            generate_tree(item_path, new_prefix)

if __name__ == "__main__":
    # Specify the directory you want to generate the tree for
    root_directory =  sys.argv[1] #"path/to/your/directory"  # Change this to your directory
    print(root_directory)
    generate_tree(root_directory)
