import statsmodels.api
import numpy


x = [1, 2, 3, 4, 5]
y = [2, 3.7, 3.9, 5, 7]
X = numpy.array(x)
# X = numpy.array(x).T
print X
print '2222222222222222222222222222222'
X = statsmodels.api.add_constant(X)
print X
results = statsmodels.api.OLS(y, X).fit()
print results.summary()

assert False


def main():
    (N, X, Y) = read_data()
    results = do_simple_regression(N, X, Y)

    # 3
    print(elice_utils.visualize(X, Y, results))

def read_data():
    # 1
    N = int(raw_input().strip())

    X = []
    Y = []
    for i in range(0, N):
        splitted = raw_input().strip().split()
        x = float(splitted[0])
        y = float(splitted[1])
        X.append(x)
        Y.append(y)

    return (N, X, Y)

def do_simple_regression(N, X, Y):
    # 2

    return results

if __name__ == "__main__":
    main()
