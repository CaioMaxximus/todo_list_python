#!/bin/sh

## Download the dependencies, check the enviroment and
# build the python app
# Add the executable to prior loading programs list
echo "Starting the building.."
echo "Downloading the dependencies"

# pip install -r requirements.txt

ACTUAL_FOLDER=$(pwd)
PATH_EXEC="${ACTUAL_FOLDER}/src/main.py"

echo "Creating auto start file ..."
echo $ACTUAL_FOLDER
echo $PATH_EXEC

LINE=3
CONTENT="PATH_EXEC=${PATH_EXEC}"
CONTENT=$(echo "$CONTENT" | sed 's/\//\\\//g')
echo "Defining path in initialization-wrapper.sh"
echo $CONTENT
sed -i "${LINE}s/.*/${CONTENT}/" initialization-wrapper.sh

echo "Copying initialization-wrapper to init.d folder"
chmod 755 initialization-wrapper.sh
sudo cp -p initialization-wrapper.sh /etc/init.d/
WRAPPER_PATH="initialization-wrapper.sh"

sudo chkconfig --add  "${WRAPPER_PATH}" ||sudo update-rc.d "${WRAPPER_PATH}" defaults

echo "Done.."
echo "Starting app.."
python3 src/main.py &
