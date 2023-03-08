
import os
import pandas as pd

df = pd.read_csv('adc.csv')

words = list(df)
def generate_response(input_text):
    for word in words:
          if word in input_text:
                response = df[word].mean()

                return response
          else:
                return "Try another variable"

print(list(df))

exit_conditions = (":q", "quit", "exit")


while True:

    query = input(" ")

    if query in exit_conditions:

        break

    else:

        print("BOT:", generate_response(query))
