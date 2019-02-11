import webbrowser

if __name__ == '__main__':
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
        for url in urls:
            webbrowser.open(url[:-1])
