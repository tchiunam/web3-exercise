from brownie import PartnerAgreement

from scripts.utility.helper import get_account


def deploy_partner_agreement():
    account = get_account()
    partner_agreement = PartnerAgreement.deploy({"from": account})
    transaction = partner_agreement.setBankName(
        "A_FAKE_NAME", {"from": account})
    transaction.wait(1)
    print(partner_agreement.getBankName())


def main():
    deploy_partner_agreement()
