#!/usr/bin/env python
import asyncio
import json
import re
import sys

from twinkly_client import TwinklyClient


async def twinkly_wrapper(host, calls):
    c = TwinklyClient(host)
    response = {}
    for func_name, args, kwargs in calls:
        try:
            f = getattr(c, func_name)
        except AttributeError:
            print(f"No such function: {func_name}")
            exit(1)
        response[func_name] = await f(*args, **kwargs)
    await c._session.close()
    return response


def main():
    commands = {
        "get_mode": "",
        "set_mode": "off|color|movie|effect|rt|demo",
        "get_brightness": "",
        "set_brightness": "1-100",
        "get_color": "",
        "set_color": "hue=0-360,saturation=0-255,value=0-255,red=0-255,green=0-255,blue=0-255,white=0-255",
        "get_device_info": "",
    }
    args = sys.argv[1:]

    if not args or args[0] == "-h":
        print("Usage: cli.py <host> [<func_name>(:arg1,kwarg=7),...]")
        print("Available functions:")
        for cmd, cmd_args in commands.items():
            print(f"{cmd}:{cmd_args}")
        print(
            "\nExample: cli.py 192.168.0.123 get_mode set_mode:color set_color:red=5,blue=10,green=255 "
            "set_brightness:50 get_brightness"
        )
        exit(0)

    host = args.pop(0)

    calls = []
    args_matches = re.findall("(\w+):?([\w=,]+)?", " ".join(args))
    for cmd, cmd_args in args_matches:
        if cmd not in commands:
            continue
        call_args = []
        call_kwargs = {}
        if cmd_args:
            for cmd_arg in cmd_args.split(","):
                if "=" in cmd_arg:
                    k, v = cmd_arg.split("=")
                    call_kwargs[k] = int(v) if v.isdigit() else v
                else:
                    call_args.append(int(cmd_arg) if cmd_arg.isdigit() else cmd_arg)
        calls.append((cmd, call_args, call_kwargs))

    print(json.dumps(asyncio.run(twinkly_wrapper(host, calls))))


if __name__ == "__main__":
    main()
