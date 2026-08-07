class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._balance = initial_balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance

# Example Usage
acc = BankAccount("Alice", 100.0)
acc.deposit(50.0)
acc.withdraw(30.0)
print(f"Balance for {acc.owner}: ${acc.get_balance()}")  # Output: $120.0