from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
import requests
from messages import UAgentResponse, UAgentResponseType, KeyValue
import os
import uuid
import json

currency_fetcher = Agent(
    name="currency_fetcher",
    seed="fetch live currency rates",
)

CURRENCY_API_URL = "http://api.exchangeratesapi.io/v1/latest?access_key=6f4e4faf0ff81455769f20d61ceed34a"
headers = {
    "content-type": "application/json",
  }

@currency_fetcher.on_interval(period=30)
async def get_currency_rates(ctx: Context):
    try:
        response = requests.request("GET", CURRENCY_API_URL, json=payload, headers=headers)
        if response.status_code != 200:
            print("SKYSCANNER STATUS CODE not 200: ", response.json())
            await ctx.send(sender, UAgentResponse(message=response.text, type=UAgentResponseType.ERROR))
            return
        currency_data = json.loads(response.text)
        timestamp = currency_data["timestamp"]
        base_currency = currency_data["base"]
        date = currency_data["date"]
        rates = currency_data["rates"]
        rates_dict = {}
        for currency, rate in rates.items():
          rates_dict[currency] = rate
    except Exception as exc:
         ctx.logger.error(exc)
