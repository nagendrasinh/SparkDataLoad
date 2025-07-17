# This is a sample Python script.
import sys

from lib import Utils
from lib.logger import Log4j


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Project : Spark Data Load.... ')
    if len(sys.argv) < 3:
        print("Usage: sdl {local,qa,prod} {load_date} : Arguments are mising")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark =Utils.get_spark_session(job_run_env)
    logger = Log4j(spark)
    print("Finish Creating spark session....")