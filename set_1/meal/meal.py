def main():
    dic_sched ={
        7: "breakfast time",
        12 :"lunch time",
        18: "dinner time"
    }
    time = input("What time is it? ")

    converted_time = convert(time)
    intTime= int(converted_time)

    if( intTime in dic_sched):
        print(dic_sched[intTime])
    elif(converted_time==intTime and intTime-1 in dic_sched):
        print(dic_sched[intTime-1])

def convert(time):
    hours, minutes = time.split(":")
    return (float(hours) + float(minutes)/60)


if __name__ == "__main__":
    main()
