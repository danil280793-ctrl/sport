
---

#### 2. Файл `workout.py`
Это основной код программы.

```python
import datetime
import os

# Настройки комплекса упражнений
WORKOUT_PLAN = [
    {"name": "Приседания", "sets": 3, "reps": 15},
    {"name": "Отжимания", "sets": 3, "reps": 10},
    {"name": "Планка", "sets": 3, "reps": "30 сек"},
    {"name": "Выпады", "sets": 3, "reps": "10 на каждую ногу"},
    {"name": "Скручивания (пресс)", "sets": 3, "reps": 20},
]

LOG_FILE = "progress.log"

def clear_screen():
    """Очистка консоли для удобства (работает на Windows и Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    print("====================================")
    print(f"📅 Тренировка на сегодня: {datetime.date.today()}")
    print("====================================\n")

def log_progress(exercise_name):
    """Записывает выполнение упражнения в файл."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Выполнено: {exercise_name}\n")

def main():
    clear_screen()
    show_welcome()
    
    print("Твой комплекс на сегодня:\n")
    
    for i, exercise in enumerate(WORKOUT_PLAN, 1):
        print(f"{i}. {exercise['name']}")
        print(f"   ➡ Подходы: {exercise['sets']}, Повторения: {exercise['reps']}")
        
        while True:
            user_input = input("   Выполнено? (y - да / n - пропустить / q - выход): ").lower().strip()
            
            if user_input == 'y':
                log_progress(exercise['name'])
                print("   ✅ Отлично!\n")
                break
            elif user_input == 'n':
                print("   ❌ Пропущено.\n")
                break
            elif user_input == 'q':
                print("\nТренировка остановлена. Возвращайся скорее!")
                return
            else:
                print("   Введи 'y', 'n' или 'q'.")

    print("====================================")
    print("🎉 Тренировка завершена! Ты молодец.")
    print("====================================")

if __name__ == "__main__":
    main()
