from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

a = Bip39MnemonicGenerator()

mnemonic = a.FromWordsNumber(words_num=12)
print(f"Mnemonic string:\n{mnemonic}")

seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Generate BIP44 master keys
bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN)

# Generate BIP44 account keys
bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)

# Generate BIP44 chain keys
bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)

# Generate the address pool (first 1 address)
for i in range(1):
    bip_obj_addr = bip_obj_chain.AddressIndex(i)
    print(f"{i}. Address private key:\n{bip_obj_addr.PrivateKey().Raw()}")
    print(f"{i}. Address:\n{bip_obj_addr.PublicKey().ToAddress()}")
    print("Now you can import this PRIVATE KEY or MNEMONIC to your metamask or trust wallet and deposit your BSC "
          "tokens like CAKE to your generated address ")
