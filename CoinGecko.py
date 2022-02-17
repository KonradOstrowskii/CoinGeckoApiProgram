from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib as plt
cg = CoinGeckoAPI()


def get_list_coin_history(vs_currency='usd'):
    data = cg.get_coins_markets(vs_currency='usd')
    output = pd.DataFrame()
    for row in data:
        output = output.append(row, ignore_index=True)
    output = output[['id', 'symbol', 'name']]
    print(output[0:20])


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


def pretify_data(data_df):
    data_df = data_df[data_df['date'].notna()]
    data_df['date'] = pd.to_datetime(data_df['date'], unit='ms')
    difference = data_df['price'].iloc[-1] - data_df['price'].iloc[0]
    return data_df


def get_5_head_echange():
    data = cg.get_exchanges_list()
    df = pd.DataFrame(
        data, columns=['name', 'trust_score', 'trust_score_rank'])
    df.set_index('name', inplace=True)
    print(df[0:5])


print("Underneath we will display a list of supported coinstheir ID, Symbol and Name. After selecting 3, we will display annual change of course")
get_list_coin_history()
print('##' * 20)
print("Now please put 3 ID from List : \n")
print('##' * 20)
first = input("\n pick 1 ID from list : ")
print('##' * 20)
second = input("\n pick 2 ID from list : ")
print('##' * 20)
third = input("\n pick 3 ID from list : ")

print('##' * 20)


if __name__ == "__main__":
    id = [first, second, third]
    vs_currency = 'usd'
    days = '366'
    for x in id:
        data_raw = get_coin_history(x, vs_currency, days)
        data_df = create_dataframe(data_raw)
        data_df = pretify_data(data_df)
        print(data_df)


print('##' * 20)
print("Below list of 5 biggest exchange with biggest Trust Score where u can with your cryptocurrencies")
get_5_head_echange()
