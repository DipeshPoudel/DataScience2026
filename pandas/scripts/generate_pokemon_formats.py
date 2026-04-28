"""
Create Parquet and ODS copies of pandas/data/pokemon.csv for tutorials.

Dependencies:
    pip install pandas pyarrow odfpy

Run from anywhere:
    python pandas/scripts/generate_pokemon_formats.py
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> int:
    try:
        import pandas as pd
    except ImportError:
        logger.error("pandas is required: pip install pandas")
        return 1

    script_dir = Path(__file__).resolve().parent
    pandas_root = script_dir.parent
    csv_path = pandas_root / "data" / "pokemon.csv"
    parquet_path = pandas_root / "data" / "pokemon.parquet"
    ods_path = pandas_root / "data" / "pokemon.ods"

    if not csv_path.is_file():
        logger.error("Missing CSV at %s", csv_path)
        return 1

    df = pd.read_csv(csv_path)
    logger.info("Read %s rows from %s", len(df), csv_path.name)

    try:
        df.to_parquet(parquet_path, index=False)
        logger.info("Wrote %s", parquet_path)
    except ImportError as e:
        logger.error(
            "Parquet export needs pyarrow (or fastparquet): pip install pyarrow. %s",
            e,
        )
        return 1

    try:
        df.to_excel(ods_path, index=False, engine="odf")
        logger.info("Wrote %s", ods_path)
    except ImportError as e:
        logger.error("ODS export needs odfpy: pip install odfpy. %s", e)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
