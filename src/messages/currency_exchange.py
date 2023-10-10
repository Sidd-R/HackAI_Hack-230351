from uagents import Model
from pydantic import Field

class CurrencyExchange(Model):
  base_currency: str = Field(description="The base currency with which the user wants to compare the currencies. For example: USD, EUR, etc.")
  target_currency: str = Field(description="The target currency the user wants to compare with the base currency. For example: USD, EUR, GBP")
  limit: float = Field(description="The value of foreign currency at or above which the user wants to get the notification. For example: 1.5, 2.0, etc.")