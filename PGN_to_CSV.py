from converter.pgn_data import PGNData
import pandas as pd

# First Program 1
# Converts PGN database into a CSV file that only includes game headers (no moves).

pgn_data = PGNData("2000_lower.pgn")
result = pgn_data.export(moves_required=False)