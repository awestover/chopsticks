import threading

def handle_click():
	def callback():
		total = 1+1
		print(total)
	t = threading.Thread(target=callback)
	t.start()


while True:
	a=input("hey")
	if a == "y":
		handle_click()
