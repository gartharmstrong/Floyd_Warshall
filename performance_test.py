from recursive_floyd import recursivepaths
import imperative_floyd
import datetime
import timeit

start_time = datetime.datetime.now()
recursivepaths("timer")
end_time = datetime.datetime.now()
print(end_time - start_time)

print(timeit.timeit(setup="from recursive_floyd import recursivepaths",stmt="recursivepaths('timer')", number=10))