# Aaron Kotz, CIS261, Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def __str__(self):
        result = ""
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                result += "* " * self.width + "\n"
            else:
                result += "* " + "  " * (self.width - 2) + "*\n"
        return result

def main():
    while True:
        print("Rectangle Calculator")
        try:
            height = int(input("Height: "))
            width = int(input("Width: "))
        except ValueError:
            print("Please enter valid integers for height and width.")
            continue

        rectangle = Rectangle(height, width)

        print(f"Height:    {rectangle.height}")
        print(f"Width:     {rectangle.width}")
        print(f"Perimeter: {rectangle.perimeter()}")
        print(f"Area:      {rectangle.area()}")
        print()
        print(rectangle)
        print("Continue? (y/n): ", end="")
        choice = input().strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()

