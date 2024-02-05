import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('stri', type=str)
    parser.add_argument('int', type=int)
    parser.add_argument('floaty', type=float)

    arg = parser.parse_args()
    print ("1:",arg.stri)
    print ("2:",arg.int)
    print ("3:",arg.floaty)

if __name__ == "__main__":
    main()