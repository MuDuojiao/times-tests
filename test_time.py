from times import compute_overlap_time, time_range

# create a test each in test_times.py for:
# two time ranges that do not overlap
# two time ranges that both contain several intervals each
# two time ranges that end exactly at the same time when the other starts

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


# two time ranges that do not overlap 
# large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
# short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
def test_overlap():
    # large = time_range("2010-01-12 10:00:00", "2010-01-12 14:00:00")
    # short = time_range("2010-01-12 14:30:00", "2010-01-12 12:00:00")
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    overlap = 0
    for start1, end1 in large:
        for start2, end2 in short:
            if start1 > end1 and start2 > end2:
                if end1 > start2 or start1 < end2:
                    overlap = 0
                else:
                    overlap = 1
            else:
                overlap = 0
    result = compute_overlap_time(large, short)
    assert result == 0
