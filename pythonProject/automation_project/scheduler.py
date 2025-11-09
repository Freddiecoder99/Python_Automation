import schedule
import time
from threading import Thread
from message_sender import send_message


def schedule_jobs(display_area):
    schedule.every(10).seconds.do(send_message, display_area)

    while True:
        schedule.run_pending()
        time.sleep(1)


def start_schedule(display_area):
    t = Thread(target=schedule_jobs, args=(display_area,))
    t.daemon = True
    t.start()
