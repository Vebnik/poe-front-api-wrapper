# libs
import logging

# module
from src.tools.ApiHelper import ApiHelper

class PoeApi:

  api_token: str

  def __init__(self, token: str) -> None:
    self.token = token

  @property
  def token(self):
    return self.api_token

  @token.setter
  def token(self, value: str):
    if self.__validate_token(value):
      self.api_token = value
    else:
      logging.critical('Not valid token')

  def __validate_token(self, token: str) -> bool:
    return ApiHelper.validate_token(token)

  # main logic
  def get_characters_list(self, acc_name: str) -> list[dict]:
    return ApiHelper.get_char(self.token, acc_name)

  def get_character_inv(self, acc_name: str, char_name: str) -> list[dict]:
    return ApiHelper.get_char_inv(self.token, acc_name, char_name)