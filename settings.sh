#!/bin/bash


cd $HOME

if [ -d ark ]; then
    echo "ark exists";
else
    echo "updating apt ..."; echo; echo;
    sudo apt update;
    echo; echo; echo "installing git ..."; echo; echo;
    sudo apt install git;
    echo; echo; echo "cloning ark ..."; echo; echo;
    git clone https://github.com/asimplebear/ark;
fi

echo; echo; echo "moving files around ..."; echo; echo;

cd $HOME/ark;

for i in $(ls -A homedir); do
    echo $i;
    cp -r ./homedir/$i $HOME;
done;

echo "done moving"; echo; echo;

echo "restartng to effect changes.";

sudo reboot;
