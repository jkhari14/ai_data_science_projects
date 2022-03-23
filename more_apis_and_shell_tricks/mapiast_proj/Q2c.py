import requests
import sys
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAACtQZgEAAAAAQIVNgCkDpAoAXWKdIfqYh8tdDr4%3DgKJqAKcWMcRkzYQKJVOIbLPNhI8kgZFIbN3ex2vDO9K8kv3Rkk"


def create_url(usernames):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/{}/tweets".format(usernames)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = f"https://api.twitter.com/2/users/by/username/{sys.argv[1]}"
    json_response = connect_to_endpoint(url, {"tweet.fields": "id"})
    user_id = json_response['data']['id']
    url2 = f"https://api.twitter.com/2/users/{user_id}/tweets"
    json_response2 = connect_to_endpoint(url2, {"tweet.fields": "created_at"})
    message = json_response2['data'][0]['text']
    message = message.replace('\n', '')
    dateTweeted = json_response2['data'][0]['created_at']
    print(dateTweeted, message)
    #print(user_id)
    #print(type(json_response))


if __name__ == "__main__":
    main()

