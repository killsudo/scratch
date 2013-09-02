def shut_down(response):
  response = response.lower()
  if response == "yes":
    return "Shutting down..."
  if response == "no":
    return "Shutdown aborted!"
  else:
    return "Sorry, I didn't understand you."

response = raw_input('Do you want to shutdown NOW? ')
print shut_down(response)