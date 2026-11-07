import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    df["Score"] = df["Score"].fillna(0)
    return df


def analyze_data(df):
    print("\n--- Basic Statistics ---")
    print(f'Average Score:{df["Score"].mean():.2f}')
    print(f'Max Score:{df["Score"].max()}')
    print(f'Min Score:{df["Score"].min()}')
    
    best_index = df["Score"].idxmax()
    best_student = df.loc[best_index , "Name"]
    print(f'Top Student:{best_student} (Score):{df["Score"].max()}')
    
    print("\n--- Average Score By Gender ---")
    print(df.groupby("Gender")["Score"].mean())
    
    
def process_and_save(df, output_path):
    df["Status"] = df["Score"].apply(lambda x: "Pass" if x>=10 else "Fail")
    
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Final Report Saved To {output_path}!")
    
    
if __name__ == "__main__"    :
    print("--- Student Grade Analyzer ---")
    
    input_file = "grades.csv"
    output_file = "final_report.csv"
    
    data = load_and_clean_data(input_file)
    analyze_data(data)
    process_and_save(data, output_file)
    