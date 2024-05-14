# Завдання 1
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

## Створення графа:

1. Додали вершини, які представляють станції.
2. Додали ребра, які представляють маршрути між станціями.

## Візуалізація графа:

1. Використовуємо spring_layout для визначення позицій вузлів.
2. Налаштовуємо вигляд вузлів, ребер і підписів.

## Аналіз графа:

1. Підраховуємо кількість вершин та ребер.
2. Виводимо списки вершин та ребер.
3. Визначаємо ступінь кожної вершини та середній ступінь.

<br><br>

# Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

## Пояснення

1. Створення графа: Ми використали дані з першого завдання для створення графа. Створюємо дві лінії маршруту.

2. Ми запускаємо алгоритми DFS та BFS для двох стартових вузлів: станції "Зарічна" (0) та "Майдан праці" (1).

3. Порівняння результатів: Ми порівняли результати обох алгоритмів і пояснили, чому шляхи відрізняються.

Алгоритм DFS досліджує якнайдалі вздовж кожної гілки, перш ніж вертатись назад, тому він може знайти довший шлях першим. Алгоритм BFS досліджує всіх сусідів на поточному рівні глибини перед переходом до вузлів на наступному рівні глибини, тому він завжди знаходить найкоротший шлях за кількістю ребер.
