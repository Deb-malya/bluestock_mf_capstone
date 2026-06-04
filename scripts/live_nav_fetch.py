import requests
import pandas as pd
from pathlib import Path

output_dir = Path("data/raw")

schemes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    try:

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            output_dir / f"{name}_nav.csv",
            index=False
        )

        print(f"Saved {name}")

    except Exception as e:
        print(f"Failed {name}: {e}")