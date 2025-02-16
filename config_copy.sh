#!/bin/sh

## Download the dependencies, check the enviroment and
# build the python app
# Add the executable to prior loading programs list
echo "Starting the building.."
echo "Creating virtual environment an downloading the dependencies"

#sudo python3 -m venv env
#pip install -r requirements.txt

ACTUAL_FOLDER=$(pwd)
PATH_EXEC="${ACTUAL_FOLDER}/init.sh"

echo "Creating auto start file ..."
echo "$ACTUAL_FOLDER"
echo "$PATH_EXEC"

LINE=2
CONTENT="PATH_EXEC=${PATH_EXEC}"
CONTENT=$(echo "$CONTENT" | sed 's/\//\\\//g')
ACTUAL_FOLDER_PATH=$(echo "$ACTUAL_FOLDER" | sed 's/\//\\\//g')
echo "$CONTENT"
sed -i "${LINE}s/.*/${CONTENT}/" init_script_caller.sh
sed -i "${LINE}s/.*/ACTUAL_FOLDER=${ACTUAL_FOLDER_PATH}/" init.sh


echo "Copying todo_service to /etc/systemd/system"
chmod 755 init.sh
echo "$PATH_EXEC" >> ~/.xprofile

echo "Done.."
echo "Starting app.."
./init.sh
