#!/usr/bin/env python3
"""Wrapper script to use vendored meson submodule."""

import sys
import os

# Add vendored meson to Python path
vendor_dir = os.path.dirname(os.path.abspath(__file__))
meson_dir = os.path.join(vendor_dir, 'meson')
sys.path.insert(0, meson_dir)

from mesonbuild import mesonmain

if __name__ == '__main__':
    sys.exit(mesonmain.main())
