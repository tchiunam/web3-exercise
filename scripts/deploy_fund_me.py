from brownie import config, network, MockV3Aggregator, FundMe

from scripts.utility.helper import LOCAL_BLOCKCHAIN_ENVIRONMENTS, deploy_mocks, get_account


def deploy_fund_me():
    account = get_account()
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    else:
        price_feed_address = config["networks"][
            network.show_active()]["eth_usd_price_feed"]
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Contract is deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
