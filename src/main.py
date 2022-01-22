import os
import dotenv
from uploader import Uploader
import json
from network import Network


def main():
    # Initialize env variables
    dotenv.load_dotenv()
    seed_phrase = os.getenv("SEED_PHRASE")
    password = os.getenv("PASSWORD")
    privkey = os.getenv("PRIVKEY")
    network = os.getenv("NETWORK")
    collection_url = os.getenv("COLLECTION")

    # Initialize
    uploader = Uploader()
    uploader.connect_metamask(seed_phrase, password, privkey)

    # Connect to the specified network - ENTER THE APPROPRIATE NETWORK
    if network and Network.is_support(network):
        target_network = Network.get(network)
        uploader.set_network(target_network['NETWORK_RPC'],
                             target_network['CHAIN_ID'])  # Custom network to add to Metamask
        uploader.open_metamask()
    # uploader.set_network("", 0, 1) # Use a default network provided by Metamask

    # Connect to OpenSea
    uploader.connect_opensea(test=True)
    uploader.set_collection_url(collection_url)

    # Upload NFT data in 'metadata.json' to OpenSea
    # MODIFY THE UPLOAD FUNCTION AND THE METADATA TO CONTAIN ANY ADDITIONAL METADATA
    metadata = json.load(open(os.path.join(os.getcwd(), "data", "metadata.json")))
    first_upload = False
    for i, data in enumerate(metadata):
        try:
            uploader.upload(os.path.join(os.getcwd(), "data", "assets", data["asset"]),
                            data["name"], data["external_link"], data["description"], data["unlockable"], data["price"])
            if first_upload:
                uploader.sign_transaction()
                first_upload = False
        except Exception as e:
            print(f"Failed to upload NFT {i} '{data['name']}' for reason '{e}'.")

    # Close
    uploader.close()


# Run main if this file is run directly
if __name__ == "__main__":
    main()
