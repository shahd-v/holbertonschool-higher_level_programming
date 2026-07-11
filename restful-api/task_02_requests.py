#!/usr/bin/python3
"""Consume JSONPlaceholder posts using the requests library."""

import csv
import json
import urllib.error
import urllib.request

try:
    import requests
except ImportError:
    class _Response:
        """Provide the small response interface used by this exercise."""

        def __init__(self, response):
            self.status_code = response.status
            self._content = response.read().decode("utf-8")

        def json(self):
            """Return the response body decoded from JSON."""
            return json.loads(self._content)

    class _RequestsFallback:
        """Provide a requests-like get method when requests is unavailable."""

        RequestException = urllib.error.URLError

        @staticmethod
        def get(url):
            """Fetch a URL and return a response-like object."""
            try:
                return _Response(urllib.request.urlopen(url))
            except urllib.error.HTTPError as error:
                return _Response(error)

    requests = _RequestsFallback()


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    try:
        response = requests.get(POSTS_URL)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
    except requests.RequestException:
        return None


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save selected fields to CSV."""
    try:
        response = requests.get(POSTS_URL)

        if response.status_code == 200:
            posts = response.json()
            data = [
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                }
                for post in posts
            ]

            with open("posts.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "title", "body"]
                )
                writer.writeheader()
                writer.writerows(data)
    except requests.RequestException:
        return None
