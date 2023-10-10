from messages import TopDestinations, UAgentResponse, CurrencyExchange
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os

# TOP_DESTINATIONS_CLIENT_SEED = os.getenv("TOP_DESTINATIONS_CLIENT_SEED", "top_destinations_client really secret phrase :)")

currency_exchange_client = Agent(
    name="currency_exchange_client",
    port=8008,
    seed="currency exchange client really secret phrase :)",
    endpoint=["http://127.0.0.1:8008/submit"],
)

fund_agent_if_low(currency_exchange_client.wallet.address())

currency_exchange_request = CurrencyExchange(base_currency="USD", target_currency="INR", limit=83.2)

@currency_exchange_client.on_interval(period=30)
async def send_message(ctx: Context):
    await ctx.send("agent1qvgr97vdextzccvgxmrjp5lfvfut8vavez8xslhfc09rmk5lusum260rlgf", currency_exchange_request)
    
@currency_exchange_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
  if msg.type == "init":
    print("init")
  else:
    ctx.logger.info(f"Received top destination options from: {msg.options}")
    # print()
    print("l")
    ctx.logger.info(f"Received top destination options from: {msg.options}")
    # ctx.send("currency_exchange", currency_exchange_request)
    
if __name__ == "__main__":
    currency_exchange_client.run()
    # await send_message() 