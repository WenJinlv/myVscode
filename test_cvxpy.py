import cvxpy as cvx

x = cvx.Variable()
y = cvx.Variable()

constrains = [ x + y == 1, 
               x - y >= 1]

obj = cvx.Minimize((x-y)**2)

prob = cvx.Problem(obj, constrains)
prob.solve()

print(prob.value)
print(x.value, y.value)