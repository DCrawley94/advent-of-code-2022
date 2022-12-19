#!/usr/bin/env bash

for f in src/*/*.py; do
    echo "formatting $f ..."
    autopep8 --in-place --aggressive --aggressive "$f"
done

for f in test/*.py; do
    echo "formatting $f ..."
    autopep8 --in-place --aggressive --aggressive "$f"
done
