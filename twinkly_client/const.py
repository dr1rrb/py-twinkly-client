"""Const for Twinkly."""

from aiohttp import ClientTimeout

# Twinkly API endpoints configuration
EP_DEVICE_INFO = "gestalt"
EP_MODE = "led/mode"
EP_BRIGHTNESS = "led/out/brightness"
EP_COLOR = "led/color"
EP_LOGIN = "login"
EP_VERIFY = "verify"

EP_TIMEOUT = ClientTimeout(
    total=3  # It on LAN, and if too long we will get warning about the update duration in logs
)
