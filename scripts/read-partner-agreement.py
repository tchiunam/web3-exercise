from brownie import PartnerAgreement


def read_partner_agreement():
    partner_agreement = PartnerAgreement[-1]
    print(partner_agreement.getBankName())


def main():
    read_partner_agreement()
