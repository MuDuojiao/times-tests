import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    # 将时间的string转化为想要的格式的datetime
    # 判断时start 在 end 之后
    if start_time < end_time:
        raise ValueError('The start time is behind end time')
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    # 时间差之间总共的秒数
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    # 相差的秒数 类型是 datetime
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    # print(large) # [('2010-01-12 10:00:00', '2010-01-12 12:00:00')]
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    # print(short) # [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    print(compute_overlap_time(large, short)) # [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
