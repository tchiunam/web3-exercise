from brownie import accounts, config, PartnerAgreement


def test_deploy():
    account = accounts.add(config["wallets"]["local-cli"][0]["private_key"])
    partner_agreement = PartnerAgreement.deploy({"from": account})
    expected = ""

    assert expected == partner_agreement.getBankName()


def test_update_bank_name():
    account = accounts.add(config["wallets"]["local-cli"][0]["private_key"])
    partner_agreement = PartnerAgreement.deploy({"from": account})
    expected = "A_FAKE_NAME"
    partner_agreement.setBankName(expected, {"from": account})

    assert expected == partner_agreement.getBankName()
