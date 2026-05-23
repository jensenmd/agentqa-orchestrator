import os

def scan_project_directory(target_path="."):
    """Scans a specified folder to find Python files needing QA analysis."""
    print(f"Scanning target directory: {os.path.abspath(target_path)}")
    python_files = []
    
    for root, dirs, files in os.walk(target_path):
        # Filter out heavy system, dependency, and configuration directories
        if any(ignored in root for ignored in ['.venv', '__pycache__', '.git', '.pytest_cache', 'node_modules']):
            continue
            
        for file in files:
            if file.endswith('.py') and file != 'file_scanner.py':
                full_path = os.path.join(root, file)
                python_files.append(full_path)
                
    return python_files

if __name__ == "__main__":
    print("--- Running External Target Project Scanner ---")
    
    # Point this "up and over" to look inside your neighbor repo
    target_project = "../qa-automation-showcase" 
    
    found_files = scan_project_directory(target_project)
    
    print(f"\nScan Complete. Found {len(found_files)} source files inside target:")
    for file_path in found_files:
        print(f" -> {file_path}")