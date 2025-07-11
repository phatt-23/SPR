from random import randint

if __name__ == "__main__":
    T = 10
    
    print(T)
    for _ in range(T):
        print()
        dest_dist = 5000
        print(dest_dist)

        curr_dist = 0
        for _ in range(100):
            dist = randint(10, 100)
            curr_dist += dist
            price = randint(100, 2000)
            print(curr_dist, price)

    
