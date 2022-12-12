# libs
import requests as req
import logging


class HttpClient:

  @staticmethod
  def get(url: str, json: bool):
    try:
      respons = req.get(url)

      if respons.status_code < 300:
        return respons.json() if json else respons.text

      logging.critical(f'Error on HttpClient req {respons.status_code}')
    except Exception as ex:
      logging.critical(ex)

  @staticmethod
  def post(url: str, json: bool, data: dict, headers: dict):
    try:
      respons = req.request('POST', url, data=data, headers=headers)
      
      print(f'on POST request {respons.status_code}')

      if respons.status_code < 300:
        return respons.json() if json else respons.text

      logging.critical(f'Error on HttpClient req {respons.status_code}')
    except Exception as ex:
      logging.critical(ex)