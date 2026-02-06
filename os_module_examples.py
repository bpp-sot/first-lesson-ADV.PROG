#!/usr/bin/env python3
"""
Comprehensive OS Module Examples
A collection of practical examples using Python's os module
"""

import os
import time

def separator(title):
    """Print a separator with a title"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)

# ============================================================================
# EXAMPLE 1: Current Directory Operations
# ============================================================================
def example_current_directory():
    separator("Example 1: Current Directory Operations")
    
    # Get current working directory
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    
    # Change directory (we'll change back after)
    original_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    print(f"Changed to: {os.getcwd()}")
    
    # Change back
    os.chdir(original_dir)
    print(f"Changed back to: {os.getcwd()}")

# ============================================================================
# EXAMPLE 2: Creating and Removing Directories
# ============================================================================
def example_directory_creation():
    separator("Example 2: Creating and Removing Directories")
    
    # Create a single directory
    test_dir = "test_directory"
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
        print(f"Created directory: {test_dir}")
    
    # Create nested directories
    nested_dir = "parent/child/grandchild"
    if not os.path.exists(nested_dir):
        os.makedirs(nested_dir)
        print(f"Created nested directories: {nested_dir}")
    
    # Remove directories (must be empty for rmdir)
    os.rmdir("parent/child/grandchild")
    os.rmdir("parent/child")
    os.rmdir("parent")
    os.rmdir(test_dir)
    print("Cleaned up test directories")

# ============================================================================
# EXAMPLE 3: Listing Directory Contents
# ============================================================================
def example_list_directory():
    separator("Example 3: Listing Directory Contents")
    
    # List current directory
    print("Contents of current directory:")
    items = os.listdir('.')
    for item in items[:10]:  # Show first 10 items
        print(f"  - {item}")
    
    if len(items) > 10:
        print(f"  ... and {len(items) - 10} more items")

# ============================================================================
# EXAMPLE 4: File and Directory Checks
# ============================================================================
def example_path_checks():
    separator("Example 4: File and Directory Checks")
    
    # Create a test file and directory
    os.makedirs("test_check_dir", exist_ok=True)
    with open("test_file.txt", "w") as f:
        f.write("Test content")
    
    # Check if paths exist
    print(f"'test_check_dir' exists: {os.path.exists('test_check_dir')}")
    print(f"'test_file.txt' exists: {os.path.exists('test_file.txt')}")
    print(f"'nonexistent' exists: {os.path.exists('nonexistent')}")
    
    # Check if path is a file or directory
    print(f"'test_file.txt' is a file: {os.path.isfile('test_file.txt')}")
    print(f"'test_file.txt' is a directory: {os.path.isdir('test_file.txt')}")
    print(f"'test_check_dir' is a directory: {os.path.isdir('test_check_dir')}")
    
    # Check if path is absolute
    print(f"'test_file.txt' is absolute: {os.path.isabs('test_file.txt')}")
    print(f"'{os.getcwd()}' is absolute: {os.path.isabs(os.getcwd())}")
    
    # Cleanup
    os.remove("test_file.txt")
    os.rmdir("test_check_dir")

# ============================================================================
# EXAMPLE 5: Path Manipulation
# ============================================================================
def example_path_manipulation():
    separator("Example 5: Path Manipulation")
    
    # Join paths
    path1 = os.path.join("folder", "subfolder", "file.txt")
    print(f"Joined path: {path1}")
    
    # Split path into directory and filename
    directory, filename = os.path.split(path1)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
    
    # Split filename and extension
    name, ext = os.path.splitext(filename)
    print(f"Name: {name}, Extension: {ext}")
    
    # Get absolute path
    abs_path = os.path.abspath(".")
    print(f"Absolute path of current dir: {abs_path}")
    
    # Get directory name and base name
    print(f"Directory name: {os.path.dirname(abs_path)}")
    print(f"Base name: {os.path.basename(abs_path)}")

# ============================================================================
# EXAMPLE 6: File Operations
# ============================================================================
def example_file_operations():
    separator("Example 6: File Operations")
    
    # Create a file
    with open("test_rename.txt", "w") as f:
        f.write("Original file")
    print("Created: test_rename.txt")
    
    # Rename file
    os.rename("test_rename.txt", "renamed_file.txt")
    print("Renamed to: renamed_file.txt")
    
    # Copy using rename (move)
    os.rename("renamed_file.txt", "moved_file.txt")
    print("Moved to: moved_file.txt")
    
    # Remove file
    os.remove("moved_file.txt")
    print("Deleted: moved_file.txt")

# ============================================================================
# EXAMPLE 7: File Statistics
# ============================================================================
def example_file_stats():
    separator("Example 7: File Statistics")
    
    # Create a test file
    with open("stats_test.txt", "w") as f:
        f.write("Some content for testing")
    
    # Get file stats
    stats = os.stat("stats_test.txt")
    
    print(f"File size: {stats.st_size} bytes")
    print(f"Last modified: {time.ctime(stats.st_mtime)}")
    print(f"Last accessed: {time.ctime(stats.st_atime)}")
    print(f"Created: {time.ctime(stats.st_ctime)}")
    print(f"File permissions (octal): {oct(stats.st_mode)}")
    
    # Get just the size
    size = os.path.getsize("stats_test.txt")
    print(f"\nFile size (using getsize): {size} bytes")
    
    # Cleanup
    os.remove("stats_test.txt")

# ============================================================================
# EXAMPLE 8: Environment Variables
# ============================================================================
def example_environment_variables():
    separator("Example 8: Environment Variables")
    
    # Get specific environment variable
    home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
    print(f"Home directory: {home}")
    
    # Get with default value
    custom_var = os.environ.get('MY_CUSTOM_VAR', 'default_value')
    print(f"Custom variable: {custom_var}")
    
    # Set environment variable
    os.environ['MY_TEST_VAR'] = 'test_value'
    print(f"Set MY_TEST_VAR to: {os.environ['MY_TEST_VAR']}")
    
    # List some environment variables
    print("\nSome environment variables:")
    for key in list(os.environ.keys())[:5]:
        print(f"  {key}: {os.environ[key]}")

# ============================================================================
# EXAMPLE 9: Walking Directory Trees
# ============================================================================
def example_directory_walk():
    separator("Example 9: Walking Directory Trees")
    
    # Create a test directory structure
    os.makedirs("walk_test/subdir1/subsubdir", exist_ok=True)
    os.makedirs("walk_test/subdir2", exist_ok=True)
    
    with open("walk_test/file1.txt", "w") as f:
        f.write("Root file")
    with open("walk_test/subdir1/file2.txt", "w") as f:
        f.write("Subdir file")
    with open("walk_test/subdir1/subsubdir/file3.txt", "w") as f:
        f.write("Deep file")
    
    # Walk the directory tree
    print("Directory tree structure:")
    for root, dirs, files in os.walk("walk_test"):
        level = root.replace("walk_test", "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 2 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
    
    # Cleanup
    os.remove("walk_test/subdir1/subsubdir/file3.txt")
    os.rmdir("walk_test/subdir1/subsubdir")
    os.remove("walk_test/subdir1/file2.txt")
    os.rmdir("walk_test/subdir1")
    os.rmdir("walk_test/subdir2")
    os.remove("walk_test/file1.txt")
    os.rmdir("walk_test")

# ============================================================================
# EXAMPLE 10: System Information
# ============================================================================
def example_system_info():
    separator("Example 10: System Information")
    
    print(f"Operating system: {os.name}")
    print(f"Path separator: '{os.sep}'")
    print(f"Line separator: {repr(os.linesep)}")
    
    if hasattr(os, 'uname'):
        uname = os.uname()
        print(f"\nSystem info:")
        print(f"  System: {uname.sysname}")
        print(f"  Node: {uname.nodename}")
        print(f"  Release: {uname.release}")
        print(f"  Machine: {uname.machine}")

# ============================================================================
# EXAMPLE 11: Working with Paths - Normalization
# ============================================================================
def example_path_normalization():
    separator("Example 11: Path Normalization")
    
    # Normalize path (removes redundant separators and up-level references)
    messy_path = "folder//subfolder/../other_folder/./file.txt"
    normalized = os.path.normpath(messy_path)
    print(f"Original path: {messy_path}")
    print(f"Normalized path: {normalized}")
    
    # Expand user home directory
    user_path = "~/documents/file.txt"
    expanded = os.path.expanduser(user_path)
    print(f"\nOriginal: {user_path}")
    print(f"Expanded: {expanded}")
    
    # Get relative path
    current = os.getcwd()
    parent = os.path.dirname(current)
    relative = os.path.relpath(current, parent)
    print(f"\nRelative path from parent to current: {relative}")

# ============================================================================
# EXAMPLE 12: Scanning Directory (with filter)
# ============================================================================
def example_scandir():
    separator("Example 12: Scanning Directory with Filters")
    
    # Create test files
    os.makedirs("scan_test", exist_ok=True)
    with open("scan_test/file1.txt", "w") as f:
        f.write("test")
    with open("scan_test/file2.py", "w") as f:
        f.write("test")
    with open("scan_test/file3.txt", "w") as f:
        f.write("test")
    os.makedirs("scan_test/subdir", exist_ok=True)
    
    # Use scandir (more efficient than listdir for getting file info)
    print("All items:")
    with os.scandir("scan_test") as entries:
        for entry in entries:
            type_str = "DIR " if entry.is_dir() else "FILE"
            print(f"  {type_str}: {entry.name}")
    
    # Filter for .txt files
    print("\nOnly .txt files:")
    txt_files = [f for f in os.listdir("scan_test") if f.endswith('.txt')]
    for f in txt_files:
        print(f"  {f}")
    
    # Cleanup
    os.remove("scan_test/file1.txt")
    os.remove("scan_test/file2.py")
    os.remove("scan_test/file3.txt")
    os.rmdir("scan_test/subdir")
    os.rmdir("scan_test")

# ============================================================================
# EXAMPLE 13: File Permissions (Unix-like systems)
# ============================================================================
def example_permissions():
    separator("Example 13: File Permissions")
    
    # Create a test file
    with open("perm_test.txt", "w") as f:
        f.write("test")
    
    # Get current permissions
    current_perms = os.stat("perm_test.txt").st_mode
    print(f"Current permissions (octal): {oct(current_perms)}")
    
    # Check if file is readable, writable, executable
    print(f"Readable: {os.access('perm_test.txt', os.R_OK)}")
    print(f"Writable: {os.access('perm_test.txt', os.W_OK)}")
    print(f"Executable: {os.access('perm_test.txt', os.X_OK)}")
    
    if os.name != 'nt':  # Unix-like systems
        # Change permissions to read-only
        os.chmod("perm_test.txt", 0o444)
        print(f"\nChanged to read-only")
        print(f"Writable now: {os.access('perm_test.txt', os.W_OK)}")
        
        # Restore write permission before cleanup
        os.chmod("perm_test.txt", 0o644)
    
    # Cleanup
    os.remove("perm_test.txt")

# ============================================================================
# EXAMPLE 14: Creating Temporary Files
# ============================================================================
def example_temp_operations():
    separator("Example 14: Temporary Directory")
    
    import tempfile
    
    # Get temporary directory
    temp_dir = tempfile.gettempdir()
    print(f"System temp directory: {temp_dir}")
    
    # Create a file in temp directory
    temp_file = os.path.join(temp_dir, "my_temp_file.txt")
    with open(temp_file, "w") as f:
        f.write("Temporary content")
    print(f"Created temp file: {temp_file}")
    
    # Check it exists
    print(f"Temp file exists: {os.path.exists(temp_file)}")
    
    # Clean up
    os.remove(temp_file)
    print("Cleaned up temp file")

# ============================================================================
# EXAMPLE 15: Finding Files Recursively
# ============================================================================
def example_find_files():
    separator("Example 15: Finding Files Recursively")
    
    # Create test structure
    os.makedirs("search_test/dir1/dir2", exist_ok=True)
    os.makedirs("search_test/dir3", exist_ok=True)
    
    with open("search_test/target.txt", "w") as f:
        f.write("found")
    with open("search_test/dir1/target.txt", "w") as f:
        f.write("found")
    with open("search_test/dir1/dir2/target.txt", "w") as f:
        f.write("found")
    with open("search_test/dir3/other.txt", "w") as f:
        f.write("other")
    
    # Find all 'target.txt' files
    print("Finding all 'target.txt' files:")
    for root, dirs, files in os.walk("search_test"):
        for file in files:
            if file == "target.txt":
                full_path = os.path.join(root, file)
                print(f"  Found: {full_path}")
    
    # Cleanup
    os.remove("search_test/target.txt")
    os.remove("search_test/dir1/target.txt")
    os.remove("search_test/dir1/dir2/target.txt")
    os.remove("search_test/dir3/other.txt")
    os.rmdir("search_test/dir1/dir2")
    os.rmdir("search_test/dir1")
    os.rmdir("search_test/dir3")
    os.rmdir("search_test")

# ============================================================================
# EXAMPLE 16: Process ID and Process Management
# ============================================================================
def example_process_info():
    separator("Example 16: Process Information")
    
    # Get current process ID
    pid = os.getpid()
    print(f"Current process ID: {pid}")
    
    # Get parent process ID
    if hasattr(os, 'getppid'):
        ppid = os.getppid()
        print(f"Parent process ID: {ppid}")
    
    # Get user ID (Unix-like systems)
    if hasattr(os, 'getuid'):
        uid = os.getuid()
        print(f"User ID: {uid}")

# ============================================================================
# EXAMPLE 17: Symbolic Links (Unix-like systems)
# ============================================================================
def example_symlinks():
    separator("Example 17: Symbolic Links")
    
    if os.name != 'nt':  # Unix-like systems
        # Create a target file
        with open("symlink_target.txt", "w") as f:
            f.write("Target content")
        
        # Create symbolic link
        os.symlink("symlink_target.txt", "symlink_link.txt")
        print("Created symbolic link: symlink_link.txt -> symlink_target.txt")
        
        # Check if it's a link
        print(f"Is symbolic link: {os.path.islink('symlink_link.txt')}")
        
        # Read the link
        link_target = os.readlink("symlink_link.txt")
        print(f"Link points to: {link_target}")
        
        # Cleanup
        os.remove("symlink_link.txt")
        os.remove("symlink_target.txt")
    else:
        print("Symbolic links example skipped (Windows system)")

# ============================================================================
# EXAMPLE 18: Directory Size Calculation
# ============================================================================
def example_directory_size():
    separator("Example 18: Calculate Directory Size")
    
    def get_directory_size(path):
        total_size = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except OSError:
                    pass
        return total_size
    
    # Create test directory with files
    os.makedirs("size_test/subdir", exist_ok=True)
    with open("size_test/file1.txt", "w") as f:
        f.write("A" * 1000)  # 1000 bytes
    with open("size_test/subdir/file2.txt", "w") as f:
        f.write("B" * 2000)  # 2000 bytes
    
    # Calculate size
    total_size = get_directory_size("size_test")
    print(f"Total directory size: {total_size} bytes")
    
    # Cleanup
    os.remove("size_test/file1.txt")
    os.remove("size_test/subdir/file2.txt")
    os.rmdir("size_test/subdir")
    os.rmdir("size_test")

# ============================================================================
# EXAMPLE 19: Safe File Operations with exist_ok
# ============================================================================
def example_safe_operations():
    separator("Example 19: Safe File Operations")
    
    # Create directory safely (won't fail if it exists)
    os.makedirs("safe_test", exist_ok=True)
    print("Created directory (or it already existed)")
    
    # Try again - won't raise an error
    os.makedirs("safe_test", exist_ok=True)
    print("Called makedirs again - no error!")
    
    # Cleanup
    os.rmdir("safe_test")

# ============================================================================
# EXAMPLE 20: Practical Example - File Organizer
# ============================================================================
def example_file_organizer():
    separator("Example 20: Practical File Organizer")
    
    # Create test files with different extensions
    os.makedirs("organize_test", exist_ok=True)
    test_files = [
        "organize_test/doc1.txt",
        "organize_test/doc2.txt",
        "organize_test/script1.py",
        "organize_test/script2.py",
        "organize_test/image1.jpg",
    ]
    
    for file in test_files:
        with open(file, "w") as f:
            f.write("test")
    
    print("Before organization:")
    print(os.listdir("organize_test"))
    
    # Organize files by extension
    for file in os.listdir("organize_test"):
        if os.path.isfile(os.path.join("organize_test", file)):
            _, ext = os.path.splitext(file)
            ext_folder = ext[1:] if ext else "other"  # Remove the dot
            
            # Create folder for this extension
            folder_path = os.path.join("organize_test", ext_folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Move file to its folder
            old_path = os.path.join("organize_test", file)
            new_path = os.path.join(folder_path, file)
            os.rename(old_path, new_path)
    
    print("\nAfter organization:")
    for root, dirs, files in os.walk("organize_test"):
        level = root.replace("organize_test", "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 2 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
    
    # Cleanup
    for ext in ["txt", "py", "jpg"]:
        for file in os.listdir(f"organize_test/{ext}"):
            os.remove(f"organize_test/{ext}/{file}")
        os.rmdir(f"organize_test/{ext}")
    os.rmdir("organize_test")

# ============================================================================
# MAIN EXECUTION
# ============================================================================
def main():
    print("\n" + "="*60)
    print("  PYTHON OS MODULE - COMPREHENSIVE EXAMPLES")
    print("="*60)
    
    examples = [
        ("Current Directory Operations", example_current_directory),
        ("Creating and Removing Directories", example_directory_creation),
        ("Listing Directory Contents", example_list_directory),
        ("File and Directory Checks", example_path_checks),
        ("Path Manipulation", example_path_manipulation),
        ("File Operations", example_file_operations),
        ("File Statistics", example_file_stats),
        ("Environment Variables", example_environment_variables),
        ("Walking Directory Trees", example_directory_walk),
        ("System Information", example_system_info),
        ("Path Normalization", example_path_normalization),
        ("Scanning Directory with Filters", example_scandir),
        ("File Permissions", example_permissions),
        ("Temporary Directory", example_temp_operations),
        ("Finding Files Recursively", example_find_files),
        ("Process Information", example_process_info),
        ("Symbolic Links", example_symlinks),
        ("Calculate Directory Size", example_directory_size),
        ("Safe File Operations", example_safe_operations),
        ("Practical File Organizer", example_file_organizer),
    ]
    
    for i, (name, func) in enumerate(examples, 1):
        try:
            func()
        except Exception as e:
            print(f"\nError in example: {e}")
        
        # Pause between examples for readability
        if i < len(examples):
            time.sleep(0.5)
    
    print("\n" + "="*60)
    print("  ALL EXAMPLES COMPLETED!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
