#!/bin/sh

echo "18 21 * * mon cd '$PWD' && ./download.py && cd downloads && git commit . -m automatic\ download && git push"
