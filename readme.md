### Результати (у секундах)
| Розмір даних | Сортування вставками | Сортування злиттям | Timsort (вбудований) |
|--------------|----------------------|--------------------|----------------------|
| 100          | 0.000174             | 0.000161           | 0.000013             |
| 1,000        | 0.021989             | 0.002180           | 0.000153             |
| 5,000        | 0.872604             | 0.017815           | 0.001087             |

### Аналіз результатів
- **Сортування вставками** показує значно гірші результати на великих обсягах даних через квадратичну складність \(O(n^2)\).
- **Сортування злиттям** має значно кращі показники, ніж сортування вставками, завдяки його логарифмічній складності \(O(n \log n)\).
- **Timsort**, який використовується в Python за замовчуванням через функцію `sorted()`, демонструє найкращі показники часу. Це пояснюється тим, що Timsort оптимізований для різних типів даних і сценаріїв, з'єднуючи переваги сортування злиттям та вставками.

Ці результати підтверджують, що Timsort є винятково ефективним для реальних даних і є оптимальним вибором для загальних задач сортування в Python.
