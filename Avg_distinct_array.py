# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

def average(array):
    return round(sum(set(array))/len(set(array)),3)

if __name__ == '__main__':
