import os
import json
import requests
from get_data import read_params
import argparse


def call_prediction_endpoint(config_path):
    config = read_params(config_path)
    json_data = ''
    payload = config["payload_dir"]
    with open(payload) as user_file:
        json_data = user_file.read()
    url = "http://localhost:5000"

    response = requests.post(url, json=json_data)
    print(response.text)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    call_prediction_endpoint(config_path=parsed_args.config)
