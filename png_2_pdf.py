#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image
import os

def main():
    file_list = os.listdir(".")
    pic_name = []
    img_list = []
    pic_name = list(filter(lambda x: x.endswith(".png"), file_list))
    pic_name = sorted(pic_name, key=lambda x: int(x.replace(".png", "")))

    img1 = Image.open(pic_name[0])
    if img1.mode == "RGBA":
        img1 = img1.convert("RGB")
    
    pic_name.pop(0)
    for img in pic_name:
        img = Image.open(img)
        if img.mode == "RGBA":
            img = img.convert("RGB")

        img_list.append(img)

    img1.save("ret.pdf", "PDF", quality=80, resolution=100.0, save_all=True, append_images=img_list)
    print("save to ret.pdf")

if __name__ == "__main__":
    main()
