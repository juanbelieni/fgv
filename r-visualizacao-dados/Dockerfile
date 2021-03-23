FROM jupyter/r-notebook:latest

RUN conda install -y -c conda-forge jupyter_contrib_nbextensions

RUN R -e "install.packages(\"formatR\", repos=\"https://cran.rstudio.com\")"

RUN R -e "install.packages(\"jsonlite\", repos=\"https://cran.rstudio.com\")"

RUN jupyter contrib nbextension install --user

CMD ["start-notebook.sh", "--notebook-dir='/home/jovyan/src'", "--NotebookApp.token=''", "--NotebookApp.password=''"]