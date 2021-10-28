from matplotlib import pyplot as plt

gamma = 0.001
current = 2  # The algorithm starts at x=6
precision = 0.000001
previous_step_size = 1
max_iters = 1000  # maximum number of iterations
iters = 0  # iteration counter
df = lambda x: 8 * x**3 - 12 * x**2 - 1
df2 = lambda x: 24 * x**2 - 24 * x

x = []
y = []
while (previous_step_size > precision) & (iters < max_iters):
    previous = current
    current -= df(previous)/df2(previous)
    previous_step_size = abs(current - previous)
    iters += 1
    x.append(iters)
    y.append(previous_step_size)
    print(previous_step_size)
    print(iters)
if iters >= max_iters:
    print("local minimum not found")
    print("value found after max iterations: ", current)
else:
    print("The local minimum occurs at:", current)
    print("Number of iterations used:", iters)

plt.plot(x[:], y[:], "-x", markersize=3, color="black", alpha=0.5, label="my graph")
plt.xlabel("iteration")
plt.ylabel("step size")
plt.legend()
plt.title("convergence plot")
plt.show()
