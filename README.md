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

#### Email Receipt Setup

First, [sign up for a SendGrid account](https://signup.sendgrid.com/), then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account.

Then [create a SendGrid API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. We'll want to store the API Key value in an [environment variable](/notes/environment-variables.md) called `SENDGRID_API_KEY`.

Also set an environment variable called `SENDER_ADDRESS` to be the same email address as the single sender address you just associated with your SendGrid account (e.g. "abc123@gmail.com").


#### Email Template Setup

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable called SENDGRID_TEMPLATE_ID.

Back in the SendGrid platform, click "Add Version" to create a new version of a "Blank Template" and select the "Code Editor" as your desired editing mechanism.

At this point you should be able to paste the following HTML into the "Code" tab, and the corresponding example data in the "Test Data" tab, and save each after you're done editing them.

Example "Code" template which will specify the structure of all emails:

```html
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}}</li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
```



Finally, configure the template's subject by clicking on "Settings" in the left sidebar. Choose an email subject like "Your Receipt from the Angel Foods Grocery". Then click "Save Template".

After configuring and saving the email template, we should be able to use it to send an email:

#### Environment Variables Setup

In the root directory of your local repository, create a new file with the name ".env." In the ".env" file, create a "TAX_RATE" variable that contains the tax rate needed for your store location in decimal format (8.75% -> 0.0875):

    TAX_RATE= 0.0875

Additionally, in the ".env" file, create a "SENDGRID_API_KEY" variable that contains your API key:

    SENDGRID_API_KEY = YOUR API KEY

Lastly, in the ".env" file, create a "SENDER_ADDRESS" variable that contains your email address associated with your SendGrid account:

    SENDER_ADDRESS = YOUR EMAIL


## Usage

Run the checkout system script in your command line:

```py
python shopping_cart.py