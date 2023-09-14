def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


def main():
    print_upper_texts("Hola", "Mundo", "Desde", "Python")
    return 0

if __name__ == '__main__':
    main()