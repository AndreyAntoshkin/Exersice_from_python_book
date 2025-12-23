# Список словарей, где каждый словарь представляет собой фотографию

photos = [
 {
  "name": "photo1.jpg",
  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
 },
 {
  "name": "photo2.jpg",
  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
 },
 {
  "name": "photo3.jpg",
  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
 },
 {
  "name": "photo4.jpg",
  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
 }
]

# объявляем словарь, где будут храниться фотографии сгруппированные по тематике
photo_groups = {}

def intersection(lst1, lst2):
 return "_".join([value for value in lst1 if value in lst2])


# Вложенная пара циклов для создания пар сравнения
for i in range (1, len(photos)):
 for j in range (i+1, len(photos) + 1):
  print(f'intersection photo {i} with photo {j}')
  lst = intersection(photos[i - 1]["tags"], photos[j-1]['tags'])
  if lst:
   n = photo_groups.setdefault(lst, list((photos[i - 1]["name"], photos[j - 1]["name"])))
print(photo_groups)

