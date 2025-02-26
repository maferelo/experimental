import datetime
import json

import pandas as pd

def get_data():
    with open("data.json", "r") as file:
        return json.load(file)
    
def parse_data_to_df(data):
    product_data = []
    for product in data:
        product_data.append({
            "id": product["productId"],
            "title": product["title"]["displayTitle"],
            "price": product["prices"]["salePrice"]["cent"] if "prices" in product else None,
            "url": product["productDetailUrl"],
            "tradeCount": int(product["trade"]["realTradeCount"]),
            "starRating": product["evaluation"]["starRating"] if "evaluation" in product else None,
            "timestamp": datetime.datetime.fromisoformat(product["timestamp"])
        })
    return pd.DataFrame.from_records(product_data).dropna()

def get_best_product(df, n=30):
    df = df.sort_values('timestamp').drop_duplicates('id', keep='last')
    df["metric"] = (df.tradeCount * df.starRating) / df.price
    df = df.sort_values(by="metric", ascending=False)
    return df[df["starRating"] >= 4.8].head(n)["url"].values

def main() -> None:
    data = get_data()
    df = parse_data_to_df(data)
    return get_best_product(df)

if __name__ == "__main__":
    main()