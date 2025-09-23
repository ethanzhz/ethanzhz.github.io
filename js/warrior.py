import time

class Warrior:
    def __init__(self, name, hp, attack, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        print(f"{self.name} 攻击了 {enemy.name}，造成 {self.attack} 点伤害！")
        enemy.hp -= self.attack
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"{enemy.name} 剩余生命值：{enemy.hp}")

# 创建两个战士
w1 = Warrior("战士A", hp=50, attack=12, speed=8)
w2 = Warrior("战士B", hp=50, attack=10, speed=10)

# 按速度决定先手
if w1.speed > w2.speed:
    attacker, defender = w1, w2
else:
    attacker, defender = w2, w1

print(f"战斗开始！{attacker.name} 速度更快，先手攻击！\n")

# 战斗循环
rounds = 1
while w1.is_alive() and w2.is_alive():
    print(f"--- 第 {rounds} 回合 ---")
    attacker.attack_enemy(defender)
    if not defender.is_alive():
        print(f"\n{defender.name} 倒下了！{attacker.name} 获胜！")
        break
    # 交换攻防
    attacker, defender = defender, attacker
    rounds += 1
    time.sleep(1)
