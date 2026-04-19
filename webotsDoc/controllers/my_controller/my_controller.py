from controller import Robot
import math

# Создаем объект робота
robot = Robot()
# Получаем базовый шаг симуляции (обычно 32 мс)
timestep = int(robot.getBasicTimeStep())

# 1. Инициализация тяговых моторов (крутят колеса)
# Проверь, что эти имена в кавычках в точности как в Webots!
drive_motor_names = ['left_front_wheel', 'right_front_wheel', 'left_back_wheel', 'right_back_wheel']
drive_motors = []

for name in drive_motor_names:
    motor = robot.getDevice(name)
    if motor:
        # ВАЖНО: Переводим мотор в режим управления скоростью
        motor.setPosition(float('inf')) 
        motor.setVelocity(0.0)
        drive_motors.append(motor)
    else:
        print(f"Ошибка: мотор {name} не найден!")

# 2. Инициализация рулевых моторов (поворачивают ось)
# У них НЕ СТАВИМ setPosition(inf), они работают по углам
left_steer = robot.getDevice('left_steer')
right_steer = robot.getDevice('right_steer')

if left_steer:
    left_steer.setPosition(0.0) # Прямо
if right_steer:
    right_steer.setPosition(0.0)

# Главный цикл
while robot.step(timestep) != -1:
    # Устанавливаем угол поворота (например, 0.3 радиана влево)
    steering_angle = 5 
    if left_steer and right_steer:
        left_steer.setPosition(steering_angle)
        right_steer.setPosition(steering_angle)
    
    # Устанавливаем скорость (например, 5.0 рад/с)
    speed = 5.0
    for motor in drive_motors:
        motor.setVelocity(speed)
        
    # Выводим время для проверки, что код вообще крутится
    print(f"Time: {robot.getTime():.2f}, Speed: {speed}")