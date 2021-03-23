FROM jupyter/scipy-notebook:latest

RUN conda install -y -c conda-forge jupyter_contrib_nbextensions yapf

RUN jupyter contrib nbextension install --user

CMD ["start-notebook.sh", "--notebook-dir='/home/jovyan/src'", "--NotebookApp.token=''", "--NotebookApp.password=''"]