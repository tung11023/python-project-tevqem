import yaml
from src.utils import process_data

def main():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    data = process_data(config["data_path"])
    print(f"Processed {len(data)} records")

if __name__ == "__main__":
    main()
