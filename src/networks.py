# Main network and testnet3 definitions

# Sibcoin src/chainparams.cpp
params = {
    'sibcoin_main': {
        'pubkey_address': 63,
        'script_address': 40,
        'genesis_hash': '00000c492bf73490420868bc577680bfc4c60116e7e85343bc624787c21efa4c'
    },
    'sibcoin_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #L210
    }
}
