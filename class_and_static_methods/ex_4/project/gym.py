from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer
from project.customer import Customer


class Gym:

    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sub = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == sub.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == sub.trainer_id), None)

        plan = next((p for p in self.plans if p.id == sub.exercise_id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

        return f"{repr(sub)}\n{repr(customer)}\n{repr(trainer)}\n{repr(equipment)}\n{repr(plan)}"
