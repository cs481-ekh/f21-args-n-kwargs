#!/bin/bash
python -m pip install --upgrade pip
pip install pylint
cd WebSearchableEquipmentDatabase || exit 1
pylint --fail-under=9 $(ls -R|grep .py$|xargs)