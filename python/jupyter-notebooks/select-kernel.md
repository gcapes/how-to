# Select a different kernel in a jupyter notebook

[Read the docs](https://ipython.readthedocs.io/en/latest/install/kernel_install.html)

## Create a venv to run the jupyter-notebook server

```shell
python -m venv venv
source venv/bin/activate 
pip install jupyter
```

## Create another venv you want available to any jupyter notebook

```shell
python -m venv venv
source venv/bin/activate 
pip install ipykernel
python -m ipykernel install --user --name myotherenv --display-name "Python (myotherenv)"
```

```output
Installed kernelspec myotherenv in /home/mbexegc2/.local/share/jupyter/kernels/myotherenv
```

This creates a new directory in `~/.local/share` for the environment.

Now, go back to your first environment, start `jupyter-notebook`  and you should have the option to access the 'myotherenv' kernel.


