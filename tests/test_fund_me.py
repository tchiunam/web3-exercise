import pytest
from brownie import accounts, exceptions
from scripts.deploy_fund_me import deploy_fund_me
from scripts.utility.helper import get_account


def test_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx_fund = fund_me.fund({"from": account, "value": entrance_fee})
    tx_fund.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx_withdraw = fund_me.withdraw({"from": account})
    tx_withdraw.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    account = accounts.add()
    fund_me = deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": account})
