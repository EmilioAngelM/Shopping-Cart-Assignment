# Shopping-Cart-Assignment

## Description

This is a store checkout system.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this remote repository https://github.com/EmilioAngelM/Shopping-Cart-Assignment under your own control, then "clone" or download your remote copy onto your local computer.

#### Environment Setup

```sh
# IF USING THIRD-PARTY PACKAGES, USE A NEW ENV:
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt #(after specifying desired packages inside)

pip install sendgrid 
```

From inside the virtual environment, install package dependencies:

```sh
pip install python-dotenv
```

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/Shopping-Cart-Assignment
```

#### Setup

In the root directory of your local repository, create a new file with the name ".env." In the ".env" file, create a "TAX_RATE" variable that contains the tax rate needed for your store location in decimal format (8.75% -> 0.0875):

    TAX_RATE= 0.0875

Additionally, in the ".env" file, create a "SENDGRID_API_KEY" variable that contains your API key:

    SENDGRID_API_KEY = YOUR API KEY

Lastly, in the ".env" file, create a "SENDER_ADDRESS" variable that contains your email address associated with your SendGrid account:

    SENDER_ADDRESS = YOUR EMAIL


## Usage

Run the checkout system script in your command line:

```py
python game.py