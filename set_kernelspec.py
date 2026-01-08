import nbformat
nb = nbformat.read('projet-sys-recommand-M2.ipynb', as_version=4)
nb.metadata['kernelspec'] = {'name':'sysrec-venv','display_name':'Python (sysrec .venv)','language':'python'}
nb.metadata['language_info'] = {'name':'python','version':'3.14'}
nbformat.write(nb, 'projet-sys-recommand-M2.ipynb')
print('notebook metadata updated: kernelspec=sysrec-venv')
