import requests
import random as rand
from pyfiglet import figlet_format


def make_joke(user_input):
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={
            "term": user_input
        }
    ).json()
    data = response['results']
    joke_list = [dic['joke'] for dic in data]
    if(len(joke_list)):
        print(f"I have {len(joke_list)} jokes. Here's one: ")
        print(rand.choice(joke_list))
    else:
        print(f"Sorry! I don't have any jokes on {user_input}. Please try again.")


if __name__ == '__main__':
    msg = "Silly Jokes!"
    print(figlet_format(msg))
    user_input = input("Let me tell you a joke! Give me a topic: ")
    make_joke(user_input)
