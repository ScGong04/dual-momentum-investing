import yaml
import yfinance as yf

with open("config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

    assets = cfg["universe"]

    risky_assets_data = {}
    
    risky_assets = assets["risky"]
    defen_assets = assets["defen"]
    start_date   = assets["start"]
    end_date     = assets["end"]

    for asset in risky_assets:
        risky_assets_data[asset] = yf.download(asset, start_date, end_date)

    



    



