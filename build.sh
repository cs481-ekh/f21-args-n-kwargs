#!/bin/bash
python -m pip install --upgrade pip || exit $?
pip install pylint || exit $?
cd WebSearchableEquipmentDatabase || exit $?
pylint --fail-under=9 $(ls -R|grep .py$|xargs) || exit $?