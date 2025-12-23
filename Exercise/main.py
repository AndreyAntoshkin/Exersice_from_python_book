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

# Вложенная пара циклов для создания пар сравнения
for i in range (len(photos)):
 for j in range (i+1, len(photos)):
  print(f'Объединение фото {i} с фото {j}')
  lst = photos[i]['tags'].intersection(photos[j]['tags'])
  print(f'Объединенные тэги у фото: {lst}')
  if lst:
   key = "_".join(sorted(lst))
   photo_groups.setdefault(key, list((photos[i]["name"], photos[j]["name"])))
print(photo_groups)

