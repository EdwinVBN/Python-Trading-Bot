import pandas as pdb

from td.client import TDClient
from td.utils import milliseconds_sinds_epoch

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union


class PyBot():


    def __init__(self, client_id: str, redirect_url: str, credentials_path: str = None, trading_account: str = None) -> None:
  