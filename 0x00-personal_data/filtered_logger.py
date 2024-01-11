#!/usr/bin/env python3
"""0. regex-ing"""

import re
import logging
from typing import (
    List,
)
from mysql.connector.connection import MySQLConnection
import os


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str) -> str:
    """returns log message obfsucated"""
    for field in fields:
        match = r'({}=)([^{}]+)'.format(field, seperator)
        message = re.sub(match, r'\1{}'.format(redaction), message)
    return message
