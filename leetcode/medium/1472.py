class BrowserHistory:

	def __init__(self, homepage: str):
		self.current_step = 0
		self.history = [homepage]
	def visit(self, url: str) -> None:
		# Truncate forward history before appending
		self.history = self.history[:self.current_step + 1]
		self.history.append(url)
		self.current_step = len(self.history) - 1

	def back(self, steps: int) -> str:
		self.current_step = max(self.current_step - steps,0)
		return self.history[self.current_step]
	def forward(self, steps: int) -> str:
		self.current_step = min(self.current_step + steps, len(self.history)-1)
		return self.history[self.current_step]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)