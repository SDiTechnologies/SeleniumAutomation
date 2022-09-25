#!/usr/bin/env python3
from traceback import print_exc
from models import *

if __name__ == "__main__":
    from samples import test_eight_components

    try:
        # test_eight_components()
        pea = PracticalExampleAutomation()
        # pea.test_page_loads()
        pea.test_fill_example()
    except Exception as e:
        print_exc()
