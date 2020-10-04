import sched
import time
import playsound

def set_alarm(alarm_time, sound_file, message):
    blocking = True
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    # s.enterabs(alarm_time, 1, playsound.playsound(sound_file, block=blocking))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    playsound.playsound(sound_file, block=blocking)
    s.run()


if __name__ == '__main__':
    set_alarm(time.time()+1, "RUN.wav", "Wake up!")