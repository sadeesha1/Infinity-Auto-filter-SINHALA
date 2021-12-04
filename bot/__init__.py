#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Dx_Doc | @Hillard_Har | @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get(""))

API_HASH = os.environ.get("")

BOT_TOKEN = os.environ.get("")

DB_URI = os.environ.get("")

USER_SESSION = os.environ.get("")

BOT_NAME = os.environ.get("BOT_NAME", "")

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "")

GROUP_USERNAME = os.environ.get("GROUP_USERNAME", "")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
