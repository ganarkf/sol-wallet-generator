#-------------------- NOTE --------------------#

# Exception Character :
# 0 (Zero), O (Letter O), I (Letter I), l (Lowercase Letter L), 1 (One)

# Note on time required for wallet generation:
# The time to generate a wallet increases exponentially with the length of the filter:
# - A 3-character filter is relatively quick and often generates a match instantly or within seconds.
# - A 4-character filter takes noticeably longer but is still manageable for most use cases.
# - A 5-character filter can take a long time (minutes to hours) depending on system performance.
# - Filters longer than 5 characters are generally impractical due to the sheer number of combinations.
# This behavior occurs because the probability of finding a match decreases as 1/(58^n), where n is the filter length.

#----------------------------------------------#

import base58
from solders.keypair import Keypair

FILTERS = ["###", "###", ...]

while True:
    account = Keypair()
    wallet_address = str(account.pubkey())

    if any(wallet_address[:len(f)].lower() == f.lower() for f in FILTERS):
        privateKey = base58.b58encode(account.secret() + base58.b58decode(wallet_address)).decode('utf-8')

        print("-" * 50)
        print(f"WALLET: {wallet_address}")
        print(f"PRIVATE KEY: {privateKey}")
        print("-" * 50)
        break