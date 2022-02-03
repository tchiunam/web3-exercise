from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = Web3.toWei(2000, "ether")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    elif network.show_active() == "ganache-local":
        return accounts.add(config["wallets"]["local-ui"][0]["private_key"])
    else:
        return accounts.add(config["wallets"]["metamask"][0]["private_key"])


def deploy_mocks():
    print(f"Deploying Mocks to network {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {
                                "from": get_account()})
    print("Mocks Deployed!")
