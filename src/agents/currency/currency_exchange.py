from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import requests
from messages import UAgentResponse, UAgentResponseType, CurrencyExchange
import os
import json

# create agent
agent = Agent(
    name="currency_fetcher",
    seed="fetch live currency rates",
)

# get api key from .env
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY", "get your own key")

CURRENCY_API_URL = "http://api.exchangeratesapi.io/v1/latest?access_key="+ CURRENCY_API_KEY

@agent.on_message(model=CurrencyExchange,replies=UAgentResponse)
async def set_values(ctx: Context, sender: str, msg: CurrencyExchange):
  # store required parameter values in the agent
  ctx.storage.set('base_currency', msg.base_currency)
  ctx.storage.set('target_currency', msg.target_currency)
  ctx.storage.set('limit', msg.limit)
  ctx.storage.set('client', sender)
  ctx.logger.info(f"Received currency exchange request from: {sender}")

@agent.on_interval(period=10)
async def get_currency_rates(ctx: Context):
  try:
    # send request to currency api
    response = requests.request(CURRENCY_API_URL)
    
    # handle error
    if response.status_code != 200:
        # send error message to client
        await ctx.send(sender, UAgentResponse(message=response.text, type=UAgentResponseType.ERROR))
        return
      
    # parse response
    currency_data = json.loads(response.text)
    timestamp = currency_data["timestamp"]
    base_currency = currency_data["base"]
    date = currency_data["date"]
    rates = currency_data["rates"]
    
    # map rates to its currency shortform
    rates_dict = {}
    for currency, rate in rates.items():
      rates_dict[currency] = rate
    
    # get parameters from agent storage
    limit = ctx.storage.get('limit')
    base_currency = ctx.storage.get('base_currency')
    target_currency = ctx.storage.get('target_currency')
    client = ctx.storage.get('client')
    
    # base currrency is EUR by default
    if base_currency != 'EUR':
      # if target currency value is above limit send alert to client 
      if rates_dict[target_currency]/rates_dict[base_currency] >= limit:
        await ctx.send(client, UAgentResponse(message=f"1 {base_currency} = {rates_dict[target_currency]/rates_dict[base_currency]} {target_currency}", type=UAgentResponseType.ALERT))
    else:
      # if target currency value is above limit send alert to client 
      if rates_dict[target_currency] >= limit:
        await ctx.send(client, UAgentResponse(message=f"1 {base_currency} = {rates_dict[target_currency]} {target_currency}", type=UAgentResponseType.ALERT))
      
  except Exception as exc:
    # handle error and send error message to client
    ctx.logger.error(message=exc,type=UAgentResponseType.ERROR)
