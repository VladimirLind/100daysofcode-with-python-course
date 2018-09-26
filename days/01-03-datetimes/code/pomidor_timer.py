import click
import datetime

@click.command()
@click.option('--work', prompt="Time to work", type=float, help='Time to work in minutes')
@click.option('--relax', prompt="Time to relax", type=float, help='Time to relax in minutes')
@click.option('--cycle', prompt="Number of cycles", type=int, help='Number of iterations to work/relax')
def pomidor_timer(work, relax, cycle):
    for i in range(0, cycle):
        print("-"*40)
        timedelta(work, "work")
        print("-"*40)
        if i != (cycle - 1):
            timedelta(relax, "have a break")
        else:
            print("you are done!")

def timedelta(time, action):
    delta = datetime.timedelta(seconds=time*60)
    now = datetime.datetime.today()
    future = now + delta
    print("time to {} for {} min".format(action, time))
    while True:
        if datetime.datetime.today() > future:
            break


if __name__ == '__main__':
    pomidor_timer()
