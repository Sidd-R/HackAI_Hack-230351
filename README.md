#  uAgent Holiday integrations Examples
### Step 1: Prerequisites
Before starting, you'll need the following:
* Python (3.8+ is recommended)
* Poetry (a packaging and dependency management tool for Python)

### Step 2: Set up .env file
To run the demo, you need API keys from:
* exchangeratesapi.io


##### OpenAI API Key
* Visit exchangeratesapi.io .
* Sign up or log in.
* Obtain your API key.

Note that if you’ve run out of exchangeratesapi credits, you will not be able to get results.

Once you have key, create a .env file in the ./src directory.
```bash
CURRENCY_API_KEY="{GET THE API KEY}"
```
To use the environment variables from .env and install the project:
```bash
cd src
poetry intall
```
### Step 3: Run the main script
To run the project and its agents:
```bash
poetry run python main.py
```
You need to look for the following output in the logs:
```
Adding currency exchange agent to Bureau: {exchange_currency_address}
```
Copy the {exchange_currency_address} value and paste it somewhere safe. You will need it in the next step.
### Step 4: Set up the client
Now that we have set up the server, let’s run the client script. To do this, replace the address in ctx.send with the value you received in the previous step in ./src/currency_exchange_client.py.

This code sends a request on startup to set the base currency, target currency and the limit for target currency which on exceeding, the client will be sent an alert. To do this, the agent on the server side sends a request to the exchange rates api every 10 seconds and when the target currency value exceeds limit, it sends a alert mesage to the agent on the client side.

### Step 5: Run the client script
Open a new terminal (let the previous one be as is), and navigate to the src folder to run the client.
```bash
cd src
poetry run python top_dest_client.py
```
Once you hit enter, a request will be sent to the top destinations agent every 10 seconds, and you will be able to see your results in the console!