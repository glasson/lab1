def input_text():
    while True:
        str=input("Ввести текст: ")
        if str!= None:
            return str

def find_comma(str):
    for i in range(len(str)):
        if str[i]==",":
            return i

def save_story(string,index):
    try:
        file = open("D:\data.txt", "a")
        file.write(string)
        file.write(" ")
        file.write(str(index))
        file.write("\n")
        file.close()
    except FileNotFoundError:
        print("Not Found File")

def show_story():
    try:
        file = open("D:\data.txt", "r")

        while True:
            string=file.readline()
            if not string:
                print("\n")
                break
            print(string,end="")
    except FileNotFoundError:
        print("Not Found File")

def main():

    i=0
    while True:
        print("Начать программу: 0\nВывести историю: 1\nЗакончить: stop")
        number=input()
        if number!="stop":
            if int(number)==0:
                string = input_text()
                if string==-1:
                    break
                index_comma = find_comma(string)
                if index_comma!= None:
                    print("Номер первой запятой",index_comma,"\n")
                    save_story(string, index_comma)
                else:
                    print("Нет запятых")

            elif int(number)==1:
                show_story()


        else:
            break







if __name__ == "__main__":
   main()