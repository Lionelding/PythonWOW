import math
import datetime
import multiprocessing as mp


# Multi-processing will have their own memory, may need Inter Process Communication 
# Multi-threading will share a common memory

def train_on_parameter(name, param):
    result = 0
    for num in param:
        result += math.sqrt(num * math.tanh(num) / math.log2(num) / math.log10(num))
    return {name: result}

def train_on_parameter_lock(name, param, result_dict, result_lock):
	result = 0
	for num in param:
		result += math.sqrt(num * math.tanh(num) / math.log2(num) / math.log10(num))
	with result_lock:
		result_dict[name] = result
	return


def main():
	start_t = datetime.datetime.now()

	num_cores = int(mp.cpu_count())

	print('total number of cores {}'.format(num_cores))
	pool = mp.Pool(num_cores)

	param_dict = {'task1': list(range(10, 30000000)),
	          'task2': list(range(30000000, 60000000)),
	          'task3': list(range(60000000, 90000000)),
	          'task4': list(range(90000000, 120000000)),
	          'task5': list(range(120000000, 150000000)),
	          'task6': list(range(150000000, 180000000)),
	          'task7': list(range(180000000, 210000000)),
	          'task8': list(range(210000000, 240000000))}	

	manager = mp.Manager()
	managed_locker = manager.Lock()
	managed_dict = manager.dict()

	# Without Manager
	results = [pool.apply_async(train_on_parameter, args=(name, param)) for name, param in param_dict.items()]

	# With Manager and Lock
	results = [pool.apply_async(train_on_parameter_lock, args=(name, param, managed_dict, managed_locker)) for name, param in param_dict.items()]
	results = [p.get() for p in results]
	print(managed_dict)

	end_t = datetime.datetime.now()
	duration = (end_t - start_t).total_seconds()
	print("Total: {}".format(duration))


if __name__ == '__main__':
	main()

	# Reference: https://zhuanlan.zhihu.com/p/93305921