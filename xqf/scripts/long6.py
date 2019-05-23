#!/usr/bin/python3

import sys
import time

TARGET_DATE = "2020-08-01 08:00:00"

TM_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_nmonth(dst):
    dst_time_str = dst
    dst_time_obj = time.strptime(dst_time_str, TM_FORMAT)
    src_time_str = time.strftime(TM_FORMAT)
    src_time_obj = time.strptime(src_time_str, TM_FORMAT)
    dst_time_obj_unix = time.mktime(dst_time_obj)
    src_time_obj_unix = time.mktime(src_time_obj)

    nsecs = dst_time_obj_unix - src_time_obj_unix
    nday = int(nsecs / (24 * 3600)) + 1
    nmonth = round(nday / 30)
    return nmonth


def main(argc, argv):
    if argc != 3:
        sys.stderr.write("Usage: %s <total> <YueZu>\n" % argv[0])
        sys.stderr.write("e.g. : %s 427 6000\n" % argv[0])
        return 1

    n_total = int(argv[1])
    yuezu  = int(argv[2])

    n_month = get_nmonth(TARGET_DATE)
    n_zufang_resv = 3
    n_zufang_cash = n_month + 1 - n_zufang_resv
    total_zujin = yuezu / 10000 * n_zufang_cash
    n_expect = n_total - total_zujin
    print("Target date        = %s" % TARGET_DATE)
    print("Months left        = %8d" % n_month)
    print("Yuezu              = %8d" % yuezu)
    print("Months Zufang(N+1) = %8d # N=%d" % (n_zufang_cash,
                                               n_zufang_cash - 1))
    print("Total   Zujin(N+1) = %8.2f" % total_zujin)
    print("TotalExpect        = %8d" % n_total)
    print("xxMinExpect        = %8.2f # %d" % (n_expect, round(n_expect)))

    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
