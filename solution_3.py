# Количество товара
books = int(input("Введите количество коробок для книг: "))
chancellery = int(input("Введите количество коробок для канцтоваров: "))
toys = int(input("Введите количество коробок для игрушек: "))

# Объём коробок для каждого типа товара
volume_books = books * 2
volume_chancellery = chancellery * 1.5
volume_toys = toys * 3

# Общий объём товаров
total_volume = volume_books + volume_chancellery + volume_toys

print(f'Объём склада равен {total_volume} куб.м.')