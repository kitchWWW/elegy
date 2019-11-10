#!/bin/bash
echo going!
python3 make.py
lilypond out.ly
open out.pdf