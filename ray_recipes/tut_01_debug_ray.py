import ray


@ray.remote
def add_2(a, b):
    res = a + b

    print(f"res is: {res}")

    return res


if __name__ == "__main__":
    future = add_2.remote(1, 2)
    result = ray.get(future)
    print(f"result is: {result}")
