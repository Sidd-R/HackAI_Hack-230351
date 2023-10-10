from uagents import Model
from enum import Enum
from typing import Optional, List

class UAgentResponseType(Enum):
  ERROR = "error"
  INIT = "init"
  ALERT = "alert"

class KeyValue(Model):
  key: str
  value: str

class UAgentResponse(Model):
  type: UAgentResponseType
  agent_address: Optional[str]
  message: Optional[str]
  options: Optional[List[KeyValue]]
  request_id: Optional[str]

# class BookingRequest(Model):
#   request_id: str
#   user_response: str
#   user_email: str
#   user_full_name: str
