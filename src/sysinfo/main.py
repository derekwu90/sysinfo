#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform


def get_platform_info():
    return platform.platform()

def main():
    print(platform.platform())
    return

if __name__ == '__main__':
    main()