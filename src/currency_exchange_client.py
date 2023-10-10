from messages import UAgentResponse, CurrencyExchange, UAgentResponseType
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os

# get seed from .env
CURRENCY_EXCHANGE_CLIENT_SEED = os.getenv("CURRENCY_EXCHANGE_CLIENT_SEED", "top_destinations_client really secret phrase :)")

# create currency exchange agent for client
currency_exchange_client = Agent(
    name="currency_exchange_client",
    port=8008,
    seed=CURRENCY_EXCHANGE_CLIENT_SEED,
    endpoint=["http://127.0.0.1:8008/submit"],
)

fund_agent_if_low(currency_exchange_client.wallet.address())

# create request object for currency exchange
currency_exchange_request = CurrencyExchange(base_currency="USD", target_currency="INR", limit=83.2)

@currency_exchange_client.on_event("startup")
async def send_message(ctx: Context):
  # send message to server to initiate currency exchange alert
  await ctx.send("{exchange_currency_address}", currency_exchange_request)
    
@currency_exchange_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
  if msg.type == UAgentResponseType.ALERT:
    #log alert message if target currency value exceeds specified limit
    ctx.logger.info(f"Alert: {msg.message}")
  elif msg.type == UAgentResponseType.ERROR:
    #log error message if any error occurs
    ctx.logger.info(f"Error: {msg.message}")
    
if __name__ == "__main__":
    currency_exchange_client.run()
