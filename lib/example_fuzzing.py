import sys

import afl

from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature

afl.init()

try:
    for line in sys.stdin:
        decode_dss_signature(line)
except ValueError:
    pass
