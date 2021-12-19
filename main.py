import speedtest
import time
import datetime

CSV_PATH = "~/data/benchmark.csv"

def get_line(test: speedtest.Speedtest):
  return ",".join(map(str, [datetime.datetime.now(), test.download(), test.upload()])) + "\n"

def main():
  test = speedtest.Speedtest()
  test.get_best_server()

  index = 0
  while True:

    # Housekeeping
    if index == 10000:
      test.get_best_server()
      index = 0
    else:
      index += 1

    try:
      with open(CSV_PATH, "a") as fp:
        fp.write(get_line(test))
    except:
      print("F")

    time.sleep(600)


if __name__ == "__main__":
  main()
