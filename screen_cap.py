#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

def main():
    page = 1
    while True:
        os.system(f"adb exec-out screencap -p > {page}.png")
        os.system("adb shell input swipe 700 250 200 250")
        page += 1

if __name__ == "__main__":
    main()