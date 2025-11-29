import os

def scan_directory(path):
    """
    Scans the directory and returns a string representation of the file tree
    and contents of key files.
    """
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."

    tree_summary = []
    key_files_content = []
    
    # Files to read content from
    KEY_FILES = [
        'package.json', 'requirements.txt', 'Dockerfile', 'docker-compose.yml',
        'Gemfile', 'pom.xml', 'build.gradle', 'go.mod', 'Cargo.toml',
        'pyproject.toml', 'setup.py', 'Makefile'
    ]

    # Walk through the directory
    for root, dirs, files in os.walk(path):
        # Exclude hidden directories and node_modules/venv
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'venv', 'env', '__pycache__']]
        
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_summary.append(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.startswith('.'):
                continue
            tree_summary.append(f"{subindent}{f}")
            
            if f in KEY_FILES:
                try:
                    with open(os.path.join(root, f), 'r', errors='ignore') as file:
                        content = file.read()
                        # Limit content length to avoid token limits
                        if len(content) > 2000:
                            content = content[:2000] + "\n... (truncated)"
                        key_files_content.append(f"\n--- Content of {f} ---\n{content}\n--- End of {f} ---\n")
                except Exception as e:
                    key_files_content.append(f"\nError reading {f}: {str(e)}\n")

    return "\n".join(tree_summary) + "\n" + "\n".join(key_files_content)
