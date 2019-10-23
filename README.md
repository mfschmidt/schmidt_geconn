To set up and run these notebooks:

    git clone https://github.com/mfschmidt/schmidt_geconn.git
    cd schmidt_geconn
    pipenv install
    pipenv shell
    jupyter nbextension enable --py --sys-prefix qgrid
    jupyter nbextension enable --py --sys-prefix widgetsnbextension
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install qgrid
    jupyter lab
