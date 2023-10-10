from uagents import Bureau

from agents.currency.currency_exchange import agent as currency_exchange_agent

if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8099/submit", port=8099)
    print(f"Adding currency exchange agent to Bureau: {currency_exchange_agent.address}")
    bureau.add(currency_exchange_agent)
    bureau.run()