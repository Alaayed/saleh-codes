import threading
class FooBar:
	def __init__(self, n):
		self.n = n
		self.first_lock = threading.Semaphore(1)
		self.second_lock = threading.Semaphore(0)

	def foo(self, printFoo: 'Callable[[], None]') -> None:

		for i in range(self.n):
			# printFoo() outputs "foo". Do not change or remove this line.
			self.first_lock.acquire()
			printFoo()
			self.second_lock.release()

	def bar(self, printBar: 'Callable[[], None]') -> None:

		for i in range(self.n):
			self.second_lock.acquire()
			printBar()
			self.first_lock.release()