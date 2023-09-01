#!/bin/bash
export TF_VARIABLES=$(cat test.json|base64)
python main.py

