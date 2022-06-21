from brownie import Market, NFT1155, NFT1155Factory,  NFT721, NFT721Factory
from scripts.useful import get_account

ACCOUNT = get_account()


def deploy_marketplace_erc721():
    marketplace_erc721 = NFT721.deploy(
        "TrendDapp",
        "TD",
        {"from": ACCOUNT},
        publish_source=True,
    )
    return marketplace_erc721


def deploy_erc721_factory():
    erc721_factory = NFT721Factory.deploy(
        {"from": ACCOUNT},
        publish_source=True,
    )
    return erc721_factory


def deploy_marketplace_erc1155():
    marketplace_erc1155 = NFT1155.deploy(
        {"from": ACCOUNT},
        publish_source=True,
    )
    return marketplace_erc1155


def deploy_erc1155_factory():
    erc1155_factory = NFT1155Factory.deploy(
        {"from": ACCOUNT},
        publish_source=True,
    )
    return erc1155_factory


def deploy_market():
    market = Market.deploy(
        {"from": ACCOUNT},
        publish_source=True,
    )
    return market


def main():
    marketplace_erc721 = deploy_marketplace_erc721()
    print(marketplace_erc721)

    erc721_factory = deploy_erc721_factory()
    print(erc721_factory)

    marketplace_erc1155 = deploy_marketplace_erc1155()
    print(marketplace_erc1155)

    erc1155_factory = deploy_erc1155_factory()
    print(erc1155_factory)

    market = deploy_market()
    print(market)
