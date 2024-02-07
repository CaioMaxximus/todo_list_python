#!/bin/sh
# chkconfig: 345 99 10
PATH_EXEC=/home/caiomaxx/Documentos/projetos/todo_list_python/src/main.py

case "$1" in
  start)
    # Executes our script
    sudo python3 "${PATH_EXEC}" "minimize"
    ;;
  *)
    ;;
esac
exit 0
