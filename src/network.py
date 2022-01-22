class Network:

    _networks = {
        'polygon-test': {
            'NETWORK_RPC': 'https://rpc-mainnet.maticvigil.com/',
            'CHAIN_ID': '80001',
            'SYMBOL': 'MATIC',
        },
        'polygon': {
            'NETWORK_RPC': 'https://rpc-mainnet.maticvigil.com/',
            'CHAIN_ID': '137',
            'SYMBOL': 'MATIC',
            'BLOCK_EXPLORER_URL': 'https://explorer.matic.network/'
        }
    }


    @staticmethod
    def is_support(network_id):
        return network_id in Network._networks.keys()

    @staticmethod
    def get(network_id):
        return Network._networks[network_id]