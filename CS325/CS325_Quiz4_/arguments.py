import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument("str", type=str)
    parser.add_argument("int", type=int)
    parser.add_argument("float", type=float)     
    
    args=parser.parse_args()
    
    print(args.str, args.int, args.float)