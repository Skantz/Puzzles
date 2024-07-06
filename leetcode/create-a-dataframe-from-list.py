import pandas as pd

def createDataframe(x: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(x, columns=["student_id", "age"])
