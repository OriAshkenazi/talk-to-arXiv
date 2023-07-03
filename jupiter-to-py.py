import requests
import nbformat
import os


def download_notebook_from_github(github_url, filename):
    raw_url = github_url.replace('github.com', 'raw.githubusercontent.com').replace('/blob', '')
    response = requests.get(raw_url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def convert_notebook_to_python(notebook_path, python_file):
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)
    code_cells = [cell for cell in notebook.cells if cell.cell_type == 'code']
    code = '\n'.join(cell.source for cell in code_cells)
    with open(python_file, 'w') as f:
        f.write(code)


# Github notebook URL
github_url = 'https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_for_knowledge_retrieval.ipynb'

# Paths for notebook and python file
notebook_file = 'notebook.ipynb'
python_file = 'code.py'

# Fetch and convert
download_notebook_from_github(github_url, notebook_file)
convert_notebook_to_python(notebook_file, python_file)

# Remove the downloaded .ipynb file if you want
os.remove(notebook_file)
