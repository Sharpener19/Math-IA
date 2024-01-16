from converter.pgn_data import PGNData
import pandas as pd

# First Program 1

pgn_data = PGNData("Raw_Data_IA.pgn")
result = pgn_data.export(moves_required=False)