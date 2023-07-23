from scripts.helpful_scripts import get_account, get_contract
from brownie import Zakarat, config, network, accounts


def deploy_our_token():
    account = get_account()
    ourtoken = Zakarat.deploy({"from": account})
    print(ourtoken.name())


def mint_token():
    account = get_account()
    ourtoken = Zakarat[-1]
    tx = ourtoken.mint(
        ourtoken.address,
        1,
        {
            "from": account,
        },
    )
    tx.wait(1)
    print("ZRT minted!")


def main():
    deploy_our_token()
    mint_token()
