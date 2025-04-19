def add_three_ccopies(List,data):
    for i in rnage(3):
        List.append(data)

def main():
    List = []
    print(List)
    add_three_ccopies(List,"Hello")
    print(List)

main();