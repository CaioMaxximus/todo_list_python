#!/bin/sh
ACTUAL_FOLDER=/home/caiomaxx/Documentos/projetos/todo_list_python
#. env/bin/activate
. "${ACTUAL_FOLDER}/todo_env/bin/activate"
python3 "${ACTUAL_FOLDER}/src/main.py" "minimize"
#/usr/bin/python3 "${ACTUAL_FOLDER}/src/main.py" "minimize"