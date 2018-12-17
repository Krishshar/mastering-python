from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)


# Sad to know it isn't supported in Windows