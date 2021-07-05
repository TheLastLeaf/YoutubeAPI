import requests
import time
import datetime

import youtube_dao


def error_check_get_items(response_json):
    if response_json.get("error"):
        raise Exception(f"error code: {response_json.get('error').get('code')}")

    return [item for item in response_json.get("items")]


def download_save_youtube_api_data(connection, channel_name, channel_id):
    params = {"key": "AIzaSyCdoZ2Y6U5D5TW5_-wm6S8t9kyodPkHRnI",
              "part": "snippet",
              "channelId": channel_id,
              "order": "date",
              "type": "video"}

    try:
        response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)
        response_items = error_check_get_items(response.json())
        row_count = connection.delete_list(channel_id)
        print(f"{channel_name} CHANNEL {row_count} VIDEOS DELETED")
        row_count = oracle_connection.insert_list(response_items)
        print(f"{channel_name} CHANNEL {row_count} VIDEOS ADDED")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    oracle_connection = youtube_dao.OracleConnection()

    lol_channel_id = "UCooLkG0FfrkPBQsSuC95L6w"
    lck_channel_id = "UCw1DsweY9b2AKGjV4kGJP1A"

    while True:
        print(datetime.datetime.now())

        download_save_youtube_api_data(oracle_connection, "LOL", lol_channel_id)
        download_save_youtube_api_data(oracle_connection, "LCK", lck_channel_id)

        time.sleep(900)
