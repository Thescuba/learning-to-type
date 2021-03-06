# Learning to Type
For most of my life I had always looked at the keyboard to type and that had held me back on how much work I felt I could get done. I had recently started learning to type without looking the the keyboard and want to make sure that I start to improve on my skill. To do this I plan on tracking all the things I type and using some magic of code, learn which word I struggle with. The words will be kept in a bank so I am able build the muscle memeory for these speific words.

Table of Contents
=================

  * [Installation](#installation)
    * [Install Python and Notebooks](#install-python-and-notebooks)
    * [Install Git](#install-git)
    * [Install pynput](#install-pynput)
  * [Getting Started](#getting-started)
    * [Run Notebooks](#run-notebooks)
  * [Start Logging](#start-logging)

# Installation

## Install Python and Notebooks
This repository contains Jupyter Notebooks to follow along with the lectures. However, there are several
packages and applications that need to be installed. It is recommended to install anaconda at (https://www.anaconda.com/download/).

## Install Git
Follow the instructions at (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Install pynput
Two ways to install pynput
 * Open terminal or cmd and run `pip install pynput`
 * Git clone from the (https://github.com/moses-palmer/pynput) and `run python setup.py install`
 
# Getting Started 

## Run Notebooks
1. Clone the repository to a desired location (E.g. `git clone https://github.com/Thescuba/data-science.git`)
2. Open jupyter labs or jupyter notebook either though anaconda navigator or terminal. 
3. Go to the repository directory

# Start Logging
To start logging your data, run logger.pyw which will actively log your keys. If you are on mac, you may need to use `sudo python3 logger.pyw` to grant permission to pynput to access your keyboard input. To pause/resume logging, press `esc`. To stop logging your keys, press the `end` key.