# libs
from fake_useragent import UserAgent

# module
from src.tools.HttpClient import HttpClient
from src.tools.api_paths import Character


class ApiHelper:
  """
  Help method for PoeApi
  """
  api_url: str = 'https://ru.pathofexile.com/'
  user_agent = UserAgent()
  
  @staticmethod
  def validate_token(token: str) -> bool:

    headers = {
      'Cookie': f'POESESSID={token}',
      'user-agent': ApiHelper.user_agent.opera
    }

    if HttpClient.post(f'{ApiHelper.api_url}{Character.GET_CHARACTERS}', True, {}, headers):
      return True
    return False

  @staticmethod
  def get_char(token: str, acc_name) -> list[dict]:
    headers = {
      'Cookie': f'POESESSID={token}',
      'user-agent': ApiHelper.user_agent.opera
    }

    payload = {'accountName': acc_name}

    return HttpClient.post(f'{ApiHelper.api_url}{Character.GET_CHARACTERS}', True, payload, headers)

  @staticmethod
  def get_char_inv(token: str, acc_name: str, char_name: str) -> list[dict]:
    headers = {
      'Cookie': f'POESESSID={token}',
      'user-agent': ApiHelper.user_agent.opera
    }

    payload = {'character': char_name, 'accountName': acc_name}

    return HttpClient.post(f'{ApiHelper.api_url}{Character.GET_ITEMS}', True, payload, headers)
