# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

from sysinfo.main import main
from sysinfo.main import get_platform_info

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
