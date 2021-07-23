from pypresence import *
import time

CLIENT_ID = ""  # Application ID

RPC = Presence(CLIENT_ID)
RPC.connect()

RPC.update(
    details="First text line",
    state="Second text line",

    # LARGE IMAGE
    large_image="maker",    # Developer Portal -> Rich Presence -> Art assets
    large_text="MAKER",

    # SMALL IMAGE
    small_image="maker",    # Developer Portal -> Rich Presence -> Art assets
    small_text="maker",

    # BUTTONS   There can be a maximum of 2 buttons
    buttons=[
        {
            "label": "Button 1",
            "url": "https://www.discord.com/",
        },
        {
            "label": "Button 2",
            "url": "https://www.discord.com/",
        },
    ]
)

while True:
    time.sleep(15)
