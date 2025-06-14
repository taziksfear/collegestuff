magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

stores = {
    'Магистр': magistr,
    'ДомКниги': domknigi,
    'БукМаркет': bukmarket,
    'Галерея': galereya
}

author = 'Маяковский'
result = [store for store, books in stores.items() if author in books]
print(result)