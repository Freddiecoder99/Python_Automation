def send_message(display_area=None):
    message = "Hello, This is your scheduled message."
    print(message)

    if display_area:
        display_area.insert("end", message + "\n")
        display_area.See("end")