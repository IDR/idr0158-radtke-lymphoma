import re
import pandas

# Script to check that each antibody name has an id (and vice versa)

# Example headers to check for:
# Experimental Condition [Secondary Antibody 4]
# match up with:
# Secondary Antibody 4 Identifier
#
# Experimental Condition [Primary Antibody 1]
# match up with:
# Primary Antibody 1 Identifier

PATTERN = re.compile(r"Experimental Condition \[(?P<primary>.+) Antibody (?P<number>.+)\]")

df = pandas.read_csv("../experimentA/idr0158-experimentA-annotation.csv",
                     header=0, dtype=str, na_filter=False)

for index, row in df.iterrows():
    for column_name in df.columns:
        m = PATTERN.match(column_name)
        if m:
            primary = m["primary"]
            number = m["number"]
            id_column_name = f"{primary} Antibody {number} Identifier"
            x = row[column_name]
            y = row[id_column_name]
            a = row[column_name].strip() != ""
            b = row[id_column_name].strip() != ""
            if a ^ b:
                print(f"Check {primary} Antibody {number} on line {index+2}")
