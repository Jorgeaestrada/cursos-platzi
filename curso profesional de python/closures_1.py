def main():
    a = 1

    def nested():
        print(a)

    return nested


main()