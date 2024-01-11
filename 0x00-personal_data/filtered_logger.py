#!/usr/bin/env python3
"""0. regex-ing"""

import re
import logging
from typing import List
import mysql.connector
import os


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, seperator: str,
        ) -> str:
    """returns log message obfsucated"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, seperator), replace(redaction), message)
