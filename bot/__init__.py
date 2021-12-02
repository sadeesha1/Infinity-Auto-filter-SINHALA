#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Dx_Doc | @Hillard_Har | @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("9956617"))

API_HASH = os.environ.get("8f6e046c7e7f35808ae11e77f1ecc890")

BOT_TOKEN = os.environ.get("2146361275:AAF3mgx16FEFiw8ug6IHyXoCZlsrMKyu-e0")

DB_URI = os.environ.get("mongodb+srv://erichdaniken:erichdaniken@cluster0.7enua.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("AQBZidX6xpS7DlheXbgjAgjnTfDl9jWSdOtTp-F0DZKdD-FEs0lkCwcNhvb3S5VvwaoV47yqoq5JGux4SwYcb577h3PrPK4Wjwrgktq9l4dtBKWCF8_25SOtHpCz2RicN6KV3B_66ZcvuL_IH6TEfBmXDWNb_IZfsAa1OYCSh_s8A8OQiMjnBhX6UwPiwfeZRMweeAul-rdspd-uvXSTxAarwSB3kTXdPbFkBejvNwqWC6iYT2V9EdyX51S9bVxm5HGGVk6LCTkNNj1fMNb5es7pYOaxFBcsLWbzZ1xC-V7UCixFPRRifaDVbLHOFo-GXZrJg_9nvPrY53xB5aVHT70oe6AmBgA")

BOT_NAME = os.environ.get("BOT_NAME", "🅷🅴🆇🅸🅽🅹    ☑️")

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "tifyny")

GROUP_USERNAME = os.environ.get("GROUP_USERNAME", "pirateslkmovies")

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
