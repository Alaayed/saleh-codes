import threading
class Foo:
	def __init__(self):
		self.first_lock = threading.Semaphore(1)
		self.second_lock = threading.Semaphore(0)
		self.third_lock = threading.Semaphore(0)
		pass

	def first(self, printFirst: 'Callable[[], None]') -> None:
		# printFirst() outputs "first". Do not change or remove this line.
		with self.first_lock:
			printFirst()
		self.second_lock.release()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		# printSecond() outputs "second". Do not change or remove this line.
		with self.second_lock:
			printSecond()
		self.third_lock.release()

	def third(self, printThird: 'Callable[[], None]') -> None:
		# printThird() outputs "third". Do not change or remove this line.
		with self.third_lock:
			printThird()