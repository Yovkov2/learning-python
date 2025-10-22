from collections import Counter, defaultdict, namedtuple

# Count how many times each word appears in a sentence
sentence = "the sorting hat sorts students into houses"
word_count = Counter(sentence.split())
print(word_count)  # {'the': 1, 'sorting': 1, ...}

# defaultdict example — automatically creates list for each key
students = defaultdict(list)
students['Gryffindor'].append('Harry')
students['Slytherin'].append('Draco')
print(students)

# namedtuple example — define a lightweight student object
Student = namedtuple('Student', ['name', 'house'])
harry = Student('Harry', 'Gryffindor')
print(harry.name, harry.house)
