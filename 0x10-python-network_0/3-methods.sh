#!/bin/bash

curl -sI "$1" | grep "Allow:" | cut -b 8-
