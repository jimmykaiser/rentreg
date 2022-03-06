import sys
import tabula
import pandas as pd

def get_pdf(filepath):
    """ 
    Get table out of pdf 
    Save as csv in the same spot
    """
    outfile = filepath.replace(".pdf", ".csv")
    dfs = tabula.read_pdf(filepath, pages="all", stream=True)
    # dfs = tabula.read_pdf(filepath, pages="1-20", stream=True)
    print(f"Extracting table from {filepath}")
    print(f"{len(dfs)} pages found")
    print("Combining tables")
    fulldf = pd.DataFrame()
    for df in dfs:
        fulldf = fulldf.append(df)
    fulldf.to_csv(outfile, index=False)
    print(f"CSV saved at {outfile}")

if __name__ == "__main__":
    filepath = sys.argv[1]
    # filepath = "data/2018-HCR-Manhattan.pdf"
    get_pdf(filepath)
