from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib as plt
import pprint
cg = CoinGeckoAPI()


def GetInfo():
    print(" ID          SYMBOL   NAME")
    print("bitcoin      btc      Bitcoin")
    print("etherum      eth      Etherum")
    print("binancecoin  bnb      BinanceCoin")
    print("litecoin     ltc      Litecoin")
    print("cardano      ada      Cardano")
    print("solana       sol      Solana")
    print("polkadot     dot      Polkadot")
    print("terra-luna   luna     Terra")
    print("avalanche-2  AVAX     Avhalanche")
    print("dogecoin     doge     Dogecoin")
    print("shiba-inu    shib     Shiba Inu")


def get_coin_history(id, vs_currency, days):
    data = cg.get_coin_market_chart_by_id(id=id, vs_currency=vs_currency,
                                          days=days)
    return data


def create_dataframe(data):

    prices_df = pd.DataFrame(data['prices'], columns=['date', 'price'])
    marketcaps_df = pd.DataFrame(
        data['market_caps'], columns=['date', 'market_cap'])
    total_volumes_df = pd.DataFrame(data['total_volumes'],
                                    columns=['date', 'total_volumes'])
    data_df = pd.merge(prices_df, marketcaps_df, on='date')
    data_df = pd.merge(data_df, total_volumes_df, on='date')
    return data_df


def pretify_data(data_df, coin_name):
    data_df = data_df[data_df['date'].notna()]
    data_df['date'] = pd.to_datetime(data_df['date'], unit='ms')

    difference = data_df['price'].iloc[-1] - data_df['price'].iloc[0]

    print(coin_name + ' difference over the year: ' + str(difference))

    return data_df


GetInfo()

first = input("\n pick 1 ID from list : ")
second = input("\n pick 2 ID from list : ")
third = input("\n pick 3 ID from list : ")
print('##' * 20)


if __name__ == "__main__":
    id = [first, second, third]
    vs_currency = 'usd'
    days = '365'
    for x in id:
        data_raw = get_coin_history(x, vs_currency, days)
        data_df = create_dataframe(data_raw)
        pretify_data(data_df, x)
        data_df
        data_df.set_index('date')['price'].plot(
            figsize=(30, 10), linewidth=5, color='maroon')
        print(data_df)
