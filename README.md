# DjangoDemo

## Neetcode 150 Guide

The purpose of this app is simply to make a simple list based structure for the Neetcode 150 guide.

Their options and splitting of categories is great, but they organize things by topic rather than difficulty.

This can demotivate newer learners who solve a few easy problems and end up immediately faced with a medium problem.

This will not be a big project and is simply for the DjangoDemo thing but I wanted to try making something that could help my friends.

## Dependencies

Unfortunately, I couldn't get the Python and Django versions to work. I tried Django 2.0.7 and 2.1.7 as those were the two mentioned. Both failed to run due to distutils and incompatability with the python version used in github codespace. That is why I used Django 3.2.25

These are the commands I ran (creating the virtual environment also didn't go smoothly because the workspace uses python 3.12.1 and the command was for python 3.8)

```.bash
virtualenv --python=python3 myvenv
source myvenv/bin/activate
pip install Django==3.2.25
```

So I used Python 3.12.1 and Django 3.2.25