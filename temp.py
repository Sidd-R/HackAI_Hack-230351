from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
import requests
from messages import Flights, UAgentResponse, UAgentResponseType, KeyValue, CurrencyExchange
import os
import uuid


FLIGHTS_SEED = os.getenv("FLIGHTS_SEED", "flights really secret phrase :)")

agent = Agent(
    name="currency_exchange_monitor",
    seed=FLIGHTS_SEED
)

fund_agent_if_low(agent.wallet.address())

@agent.on_message(model=CurrencyExchange,replies=UAgentResponse)
async def get_update(ctx: Context, sender: str, msg: CurrencyExchange):
  ctx.logger.info(f"Received currency exchange request from: {sender}")
  print(CurrencyExchange)

# agent.include(flights_protocol)
